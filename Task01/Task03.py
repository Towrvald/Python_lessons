# Метод трапеций
from math import exp


def func(x):
    return exp(x)


class Trap:
    def __init__(self, h, n):
        self.h = h
        self.n = n

    def CalcInt(self, h):
        x = h / 2
        sum = 0
        while x < 1:
            sum += (h / 2) * (func((x + h / 2)) + func((x - h / 2)))
            x += h
        return sum

    def GetInt(self):
        h = self.h
        for i in range(self.n):
            sum = self.CalcInt(h)
            error = abs(sum - (func(1) - func(0)))
            print('h =', h, ' error =', error)
            h = h / 10


result = Trap(0.1, 9)
result.GetInt()
