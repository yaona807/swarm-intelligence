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
def velocity_update(w, c1, c2, swarm):
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

        restriction_velocity(swarm, swarm.particles[i])


# 位置の更新
def position_update(swarm):
    for i in range(swarm.particle_num):
        x = swarm.particles[i].position
        v = swarm.particles[i].velocity

        swarm.particles[i].position = x + v

        restriction_position(swarm, swarm.particles[i])


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
