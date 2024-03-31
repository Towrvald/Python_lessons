# Метод левых прямоугольников
from math import exp


def func(x):
    return exp(x)


class LeftRec:  # Передаём шаг h, n- сколько раз уменьшаем h
    def __init__(self, h, n):
        self.h = h
        self.x = 0
        self.n = n

    def calc_int(self, h):
        x = self.x
        sum = 0
        while x <= 1:
            sum += func(x) * h
            x += h
        return sum

    def get_int(self):
        h = self.h
        for i in range(self.n):
            sum = self.calc_int(h)
            error = abs(sum - (func(1) - func(0)))
            print('h = ', h, ' error = ', error)
            h = h / 10


result = LeftRec(0.1, 9)
result.get_int()
