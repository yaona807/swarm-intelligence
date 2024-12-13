# -*- coding: utf-8 -*-

from backend.pso import calculator as calc

""" 
PSOクラス

PSOの型を定義する
-----------------------------
引数
swarm		: 粒子群クラス
function	: 関数
weight		: 重み
c1			: 速度更新式用定数
c2			: 速度更新式用定数
-----------------------------
インスタンス変数
swarm
function
weight
c1
c2
"""


class PSO:

    def __init__(self, swarm, function, weight=0.729, c1=1.4955, c2=1.4955):

        self.swarm = swarm
        self.function = function
        self.weight = weight
        self.c1 = c1
        self.c2 = c2

    # シミュレーション
    def simulate(self, iteration):
        for i in range(iteration):
            calc.evaluate(self.function, self.swarm)

            calc.velocity_update(self.weight, self.c1, self.c2, self.swarm)

            calc.position_update(self.swarm)

            print(f"\rNow Simulating(PSO) : {(i*100 + iteration)//iteration}%", end="")

        print()

        return self.swarm.global_cost
