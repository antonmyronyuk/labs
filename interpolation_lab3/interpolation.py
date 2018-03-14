import numpy as np


class Interpolation:
    def __init__(self, function, xmin=0.0, xmax=1.0, steps=10):
        diff = (xmax - xmin) / steps
        self.args = np.arange(xmin, xmax + diff, diff)
        self.func = function

    def lagrange(self, x):
        res = 0.0
        for x_i in self.args:
            mult = 1
            for x_j in self.args:
                mult *= 1 if x_i == x_j else\
                    (x - x_j) / (x_i - x_j)
            res += self.func(x_i) * mult

        return res

    def newton(self, x):
        def f(xx):
            if not isinstance(xx, np.ndarray):
                return self.func(xx)
            cur = 0.0
            for x_i in xx:
                mult = 1
                for x_j in xx:
                    mult *= 1 if x_i == x_j\
                        else (x_i - x_j)
                cur += self.func(x_i) / mult
            return cur

        res = f(self.args[0])
        term = 1.0
        for i, x_i in enumerate(self.args[:-1], 2):
            term *= (x - x_i)
            res += f(self.args[:i]) * term

        return res
