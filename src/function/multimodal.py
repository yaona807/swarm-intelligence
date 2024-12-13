# -*- coding: utf-8 -*-

import numpy as np


# 関数クラス
# それぞれがもつx_min,x_maxは実行可能領域を指す
class TheNthPowerOfTwoMinma:

    def __init__(self, x_min=-5.0, x_max=5.0):

        self.x_max = x_max
        self.x_min = x_min

    def calculate(self, x):

        ans = pow(x, 4) - 16 * pow(x, 2) + 5 * x

        return np.sum(ans)


class Ackley:

    def __init__(self, x_min=-32.768, x_max=32.768):

        self.x_max = x_max
        self.x_min = x_min

    def calculate(self, x):

        d = len(x)

        ans = (
            20
            - 20 * np.exp(-0.2 * np.sqrt(np.sum(pow(x, 2)) / d))
            + np.e
            - np.exp(np.sum(np.cos(2 * np.pi * x)) / d)
        )

        return np.sum(ans)


class Rastrigin:

    def __init__(self, x_min=-5.12, x_max=5.12):

        self.x_max = x_max
        self.x_min = x_min

    def calculate(self, x):

        ans = pow(x, 2) - 10 * np.cos(2 * np.pi * x) + 10

        return np.sum(ans)


class Griewank:

    def __init__(self, x_min=-600.0, x_max=600.0):

        self.x_max = x_max
        self.x_min = x_min

    def calculate(self, x):

        d = len(x)

        ans = (
            1
            + (np.sum(np.square(x)) / 4000)
            - np.prod(np.cos(x / np.sqrt(np.arange(1, d + 1))))
        )

        return np.sum(ans)


class Schwefel:

    def __init__(self, x_min=-500.0, x_max=500.0):

        self.x_max = x_max
        self.x_min = x_min

    def calculate(self, x):

        d = len(x)

        ans = 418.9829 * d - np.sum(x * np.sin(np.sqrt(np.abs(x))))

        return np.sum(ans)
