# Метод Монте-Карло
from math import exp
import random


class MonteCarlo:
    def __init__(self, n):  # количество генерируемых точек
        self.n = n

    def calc_int(self, n):
        sum = 0
        for _ in range(n):
            x = random.uniform(0, 1)
            sum += exp(x)
        return sum / n

    def get_int(self):
        for i in range(1, self.n + 1):
            sum = self.calc_int(10 ** i)
            error = abs(sum - (exp(1) - exp(0)))
            print('n = 10^', i, ' error =', error)


result = MonteCarlo(10)
result.get_int()
