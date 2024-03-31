# Задача 3.1
from math import exp


def func(x):
    return exp(x)


class Derivative:
    def __init__(self, x, h, n=9):
        self.h = h
        self.x = x
        self.n = n

    def calc(self, h, x):
        res = (func(x + h) - func(x)) / h
        return res

    def get_der(self):
        h = self.h
        x = self.x
        for _ in range(self.n):
            print('h = ', h, ' error = ', abs(self.calc(h, x) - func(x)))
            h /= 10


result = Derivative(1, 0.1)
result.get_der()
