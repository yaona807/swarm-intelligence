# -*- coding: utf-8 -*-

import numpy as np


class Sphere:

    def __init__(self, x_min=-5.0, x_max=5.0):

        self.x_max = x_max
        self.x_min = x_min

    def calculate(self, x):
        ans = np.sum(np.square(x))

        return ans


class Rosenbrock:

    def __init__(self, x_min=-5.0, x_max=5.0):

        self.x_max = x_max
        self.x_min = x_min

    def calculate(self, x):

        d = len(x)

        ans = 100 * pow(x[1:d] - pow(x[0 : d - 1], 2), 2) + pow(x[0 : d - 1] - 1, 2)

        return np.sum(ans)
