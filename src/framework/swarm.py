# -*- coding: utf-8 -*-
""" 
粒子群クラス

粒子群の持つ情報を定義する
------------------------------------------------------
引数
dimentions 			: 次元数
particle_num		: 粒子数
velocity_max		: 最大速度
velocity_min		: 最小速度
position_max		: 最大位置
position_min		: 最小位置
init_velocity_zero	: 速度をゼロ初期化するかのフラグ
------------------------------------------------------
インスタンス変数
global_best			: グローバルベスト
global_cost			: 最良値
"""

import numpy as np
from framework.particle import Particle


class Swarm:

    def __init__(
        self,
        dimentions=2,
        particle_num=30,
        velocity_max=1.0,
        velocity_min=-1.0,
        position_max=5.0,
        position_min=-5.0,
        init_velocity_zero=False,
    ):

        self.dimentions = dimentions
        self.particle_num = particle_num
        self.velocity_max = velocity_max * np.ones(self.dimentions)
        self.velocity_min = velocity_min * np.ones(self.dimentions)
        self.position_max = position_max * np.ones(self.dimentions)
        self.position_min = position_min * np.ones(self.dimentions)
        self.global_best = float("inf") * np.ones(self.dimentions)
        self.global_cost = float("inf")
        self.global_cost_hist = []
        self.particles = []

        for _ in range(self.particle_num):
            self.particles.append(
                Particle(
                    self.dimentions,
                    self.velocity_max,
                    self.velocity_min,
                    self.position_max,
                    self.position_min,
                    init_velocity_zero,
                )
            )
