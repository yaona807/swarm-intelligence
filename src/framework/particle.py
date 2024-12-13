# -*- coding: utf-8 -*-

""" 
粒子クラス

粒子の持つ情報を定義する
------------------------------------------------------
引数
dimentions 			: 次元数
velocity_max		: 最大速度
velocity_min		: 最小速度
position_max		: 最大位置
position_min		: 最小位置
init_velocity_zeto	: 速度をゼロ初期化するかのフラグ
------------------------------------------------------
インスタンス変数
velocity
position
personal_best		: パーソナルベスト
personal_cost		: パーソナルベストでの最良値
"""
import numpy as np


class Particle:

    def __init__(
        self,
        dimentions,
        velocity_max,
        velocity_min,
        position_max,
        position_min,
        init_velocity_zero,
    ):
        # 速度の初期化(True:ゼロ初期化 False:ランダム初期化)
        if init_velocity_zero:
            self.velocity = np.zeros(dimentions)
        else:
            self.velocity = np.random.uniform(velocity_min, velocity_max, dimentions)

        self.position = np.random.uniform(position_min, position_max, dimentions)
        self.personal_cost = float("inf")
        self.personal_best = self.position
