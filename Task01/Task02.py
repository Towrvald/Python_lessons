# Метод центральных прямоугольников
from math import exp


def func(x):
    return exp(x)


class MidRec:
    def __init__(self, h, n):
        self.h = h
        self.x = 0
        self.n = n

    def CalcInt(self, h):
        x = self.x + h / 2
        sum = 0
        while x <= 1:
            sum += func(x) * h
            x += h
        return sum

    def GetInt(self):
        h = self.h
        for i in range(self.n):
            sum = self.CalcInt(h)
            error = abs(sum - (func(1) - func(0)))
            print('h = ', h, ' error = ', error)
            h = h / 10


result = MidRec(0.1, 9)
result.GetInt()
