from math import *


def func(x):
    return exp(x)


class Runge:
    def __init__(self, h, a, b, eps):  # интегрирование в диапазоне [a, b] с шагом h
        self.h = h
        self.a = a
        self.b = b
        self.eps = eps  # точность, которую нужно получить

    def integer(self, h):
        sum = 0
        a = self.a
        b = self.b
        x = a + h
        while x < b:
            sum += (5 * func(x - h * sqrt(0.6) / 2) + 8 * func(x) + 5 * func(x + h * sqrt(0.6) / 2)) / 18
            x += h
        return h * sum

    def runge(self):  # Уменьшает h до тех пор, пока не достигнем нужной точности R (R<=eps)
        eps = self.eps
        h = self.h
        while True:
            R = abs((self.integer(h) - self.integer(2 * h)) / 127)
            if R > eps:
                h /= 2

            if R <= eps:
                print(f'Достигнута нужна точность при h = {h}')
                print(f'Значение интеграла: {self.integer(h)}')
                print(f'Погрешность: {R}')
                break
        return 0


a = Runge(0.1, 0, 1, 10 ** -8)
a.runge()
