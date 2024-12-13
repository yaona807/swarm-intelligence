# -*- coding: utf-8 -*-

import numpy as np


# 評価関数の計算
def evaluate(f, swarm, iteration, T2, a2):
    for i in range(swarm.particle_num):
        ans = f.calculate(swarm.particles[i].position)

        d2, gbest_dist = calc_interparticle_distance(
            T2, iteration, a2, swarm, swarm.particles[i]
        )

        if gbest_dist >= d2:
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
def velocity_update(w, c1, c2, swarm, iteration, T1, a1):
    d = swarm.dimentions
    gbest = swarm.global_best

    for i in range(swarm.particle_num):
        rand1 = np.random.uniform(0, 1, d)
        rand2 = np.random.uniform(0, 1, d)
        pbest = swarm.particles[i].personal_best
        x = swarm.particles[i].position
        v = swarm.particles[i].velocity

        swarm.particles[i].velocity = (
            w * v + c1 * rand1 * (pbest - x) + c2 * rand2 * (gbest - x)
        )

        d1, gbest_dist = calc_interparticle_distance(
            T1, iteration, a1, swarm, swarm.particles[i]
        )

        if gbest_dist <= d1:
            velocity_add_random(swarm, swarm.particles[i], iteration, T1)

        restriction_velocity(swarm, swarm.particles[i])


# 位置更新
def position_update(swarm):
    for i in range(swarm.particle_num):
        x = swarm.particles[i].position
        v = swarm.particles[i].velocity

        swarm.particles[i].position = x + v

        restriction_position(swarm, swarm.particles[i])


# 粒子間距離の計算
def calc_interparticle_distance(T, iteration, a, swarm, particle):
    if iteration > T:
        gbest_dist = np.linalg.norm(particle.position - swarm.global_best)

        return 0, gbest_dist

    max_dist = swarm.max_dist

    dist = ((T - iteration) * a * max_dist) / T

    gbest_dist = np.linalg.norm(
        (particle.position + particle.velocity) - swarm.global_best
    )

    return dist, gbest_dist


# 乱数加算に利用する調整変数の計算
def calc_adjust_value(T1, iteration, position_max, position_min):
    if iteration > T1:
        return 0

    adjust_value = ((T1 - iteration) * 0.5 * (position_max - position_min)) / T1

    return adjust_value


# 速度に乱数加算
def velocity_add_random(swarm, particle, iteration, T1):
    n = np.random.randn()

    adjust_value = calc_adjust_value(
        T1, iteration, swarm.position_max, swarm.position_min
    )

    particle.velocity += adjust_value * n


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
