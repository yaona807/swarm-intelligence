# -*- coding: utf-8 -*-

import numpy as np


# 評価関数の計算
def evaluate(f, swarm):
    for i in range(swarm.particle_num):
        ans = f.calculate(swarm.particles[i].position)

        pbest_update(ans, swarm, swarm.particles[i])


# pbestの更新
def pbest_update(ans, swarm, particle):
    if ans < particle.personal_cost:
        particle.personal_cost = ans
        particle.personal_best = particle.position

        gbest_update(ans, swarm, particle)


# gbestの更新
def gbest_update(ans, swarm, particle):
    if ans < swarm.global_cost:
        swarm.global_cost = ans
        swarm.global_best = particle.position


# 速度の更新
def velocity_update(
    weight_min, weight_max, c1, c2, swarm, iteration, T_BPSO, iteration_max
):
    # motion選択
    if should_convergent(T_BPSO, iteration):
        convergent_motion_velocity_update(
            weight_min, weight_max, c1, c2, swarm, iteration, iteration_max
        )

    else:
        divergent_motion_velocity_update(
            weight_min, weight_max, c1, c2, swarm, iteration, iteration_max
        )


# convergent_motion(PSO)の速度更新
def convergent_motion_velocity_update(
    weight_min, weight_max, c1, c2, swarm, iteration, iteration_max
):
    d = swarm.dimentions
    gbest = swarm.global_best
    w = weight_max - ((weight_max - weight_min) / iteration_max) * iteration

    for i in range(swarm.particle_num):
        rand1 = np.random.uniform(0, 1, d)
        rand2 = np.random.uniform(0, 1, d)
        pbest = swarm.particles[i].personal_best
        x = swarm.particles[i].position
        v = swarm.particles[i].velocity

        swarm.particles[i].velocity = (
            w * v + c1 * rand1 * (pbest - x) + c2 * rand2 * (gbest - x)
        )

        restriction_velocity(swarm, swarm.particles[i])


# divergent_motion(BPSO)の速度更新
def divergent_motion_velocity_update(
    weight_min, weight_max, c1, c2, swarm, iteration, iteration_max
):
    d = swarm.dimentions
    w = weight_max - ((weight_max - weight_min) / iteration_max) * iteration
    pbest_average = swarm.pbest_average
    position_average = swarm.position_average

    for i in range(swarm.particle_num):
        rand1 = np.random.uniform(0, 1, d)
        rand2 = np.random.uniform(0, 1, d)
        x = swarm.particles[i].position
        v = swarm.particles[i].velocity

        swarm.particles[i].velocity = (
            w * v
            + c1 * rand1 * (pbest_average - x)
            + c2 * rand2 * (position_average - x)
        )

        restriction_velocity(swarm, swarm.particles[i])


# 位置更新
def position_update(swarm):
    for i in range(swarm.particle_num):
        x = swarm.particles[i].position
        v = swarm.particles[i].velocity

        swarm.particles[i].position = x + v

        restriction_position(swarm, swarm.particles[i])


# motion選択
def should_convergent(T_BPSO, iteration):
    if iteration >= T_BPSO:
        # convergent motion
        return True
    else:
        # divergent motion
        return False


# boidsルールの計算
def calc_boids_rule(swarm, iteration, T_BPSO):
    # cohesionルールの計算
    def calc_cohesion_rule(swarm):
        total = 0

        for i in range(swarm.particle_num):
            total += swarm.particles[i].position

        return total / swarm.particle_num

    # alignmentルールの計算
    def calc_alignment_rule(swarm):
        total = 0

        for i in range(swarm.particle_num):
            total += swarm.particles[i].personal_best

        return total / swarm.particle_num

    # boidsルールを計算すべきか判別
    if should_convergent(T_BPSO, iteration):
        return 0, 0

    pbest_average = calc_alignment_rule(swarm)
    position_average = calc_cohesion_rule(swarm)

    swarm.pbest_average = pbest_average
    swarm.position_average = position_average


# 速度制限
def restriction_velocity(swarm, particle):
    particle.velocity = np.where(
        particle.velocity < swarm.velocity_max, particle.velocity, swarm.velocity_max
    )

    particle.velocity = np.where(
        particle.velocity > swarm.velocity_min, particle.velocity, swarm.velocity_min
    )


# 位置制限
def restriction_position(swarm, particle):
    particle.position = np.where(
        particle.position < swarm.position_max, particle.position, swarm.position_max
    )

    particle.position = np.where(
        particle.position > swarm.position_min, particle.position, swarm.position_min
    )
