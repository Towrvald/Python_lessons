# Метод Симпсона
from math import exp


class Simpson:
    def __init__(self, h, n):
        self.h = h
        self.n = n

    def calc_int(self, h):
        x = h / 2
        sum = 0
        while x < 1:
            sum += (1 / 6) * (exp(x - (h / 2)) + (4 * exp(x)) + exp(x + (h / 2))) * h
            x += h
        return sum

    def get_int(self):
        h = self.h
        for i in range(self.n):
            sum = self.calc_int(h)
            error = abs(sum - (exp(1) - exp(0)))
            print('h =', h, ' error =', error)
            h = h / 10


result = Simpson(0.1, 9)
result.get_int()
