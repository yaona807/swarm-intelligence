# -*- coding: utf-8 -*-

import numpy as np
from backend.psovc import calculator as calc

""" 
PSOVCクラス

PSOVCの型を定義する
----------------------------------------------
引数
swarm		: 粒子群クラス
function	: 関数
weight		: 重み
c1			: 速度更新式用定数
c2			: 速度更新式用定数
a1			: 乱数加算用定数
a2			: pbest更新抑制用定数
T1_ratio	: 乱数加算期間を決める倍率
T2_ratio	: pbest更新抑制期間を決める倍率
----------------------------------------------
インスタンス変数
swarm
function
weight
c1
c2
a1
a2
T1_ratio
T2_ratio
T1
T2
"""


class PSOVC:

    def __init__(
        self,
        swarm,
        function,
        weight=0.729,
        c1=1.4955,
        c2=1.4955,
        a1=0.05,
        a2=0.1,
        T1_ratio=0.75,
        T2_ratio=0.75,
    ):

        self.swarm = swarm
        self.function = function
        self.weight = weight
        self.c1 = c1
        self.c2 = c2
        self.a1 = a1
        self.a2 = a2
        self.T1_ratio = T1_ratio
        self.T2_ratio = T2_ratio
        self.swarm.max_dist = np.linalg.norm(swarm.position_max - swarm.position_min)

    # シミュレーション
    def simulate(self, iteration):
        self.T1 = iteration * self.T1_ratio
        self.T2 = iteration * self.T2_ratio

        for i in range(iteration):
            calc.evaluate(self.function, self.swarm, i, self.T2, self.a2)

            calc.velocity_update(
                self.weight, self.c1, self.c2, self.swarm, i, self.T1, self.a1
            )

            calc.position_update(self.swarm)

            print(
                f"\rNow Simulating(PSOVC) : {(i*100 + iteration)//iteration}%", end=""
            )

        print()

        return self.swarm.global_cost
