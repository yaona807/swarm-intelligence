# -*- coding: utf-8 -*-

from backend.bpso import calculator as calc

""" 
BPSOクラス

BPSOの型を定義する
----------------------------------------------
引数
swarm			: 粒子群クラス
function		: 関数
weight_max		: 重みの最大値
weight_min		: 重みの最小値
c1				: 速度更新式用定数
c2				: 速度更新式用定数
T_BPSO_ratio	: BPSO実行期間を決める倍率
----------------------------------------------
インスタンス変数
swarm
function
weight_max
weight_min
c1
c2
T_BPSO_ratio
T_BPSO
"""


class BPSO:

    def __init__(
        self,
        swarm,
        function,
        weight_max=0.9,
        weight_min=0.4,
        c1=2.0,
        c2=2.0,
        T_BPSO_ratio=0.5,
    ):

        self.swarm = swarm
        self.function = function
        self.weight_max = weight_max
        self.weight_min = weight_min
        self.c1 = c1
        self.c2 = c2
        self.T_BPSO_ratio = T_BPSO_ratio

    # シミュレーション
    def simulate(self, iteration):
        self.T_BPSO = iteration * self.T_BPSO_ratio

        for i in range(iteration):
            calc.evaluate(self.function, self.swarm)

            calc.calc_boids_rule(self.swarm, i, self.T_BPSO)

            calc.velocity_update(
                self.weight_min,
                self.weight_max,
                self.c1,
                self.c2,
                self.swarm,
                i,
                self.T_BPSO,
                iteration,
            )

            calc.position_update(self.swarm)

            print(f"\rNow Simulating(BPSO) : {(i*100 + iteration)//iteration}%", end="")

        print()

        return self.swarm.global_cost
