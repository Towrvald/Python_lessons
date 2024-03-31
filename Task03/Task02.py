from math import exp


def func(x):
    return exp(x)


class Derivative:
    def __init__(self, x, h, eps):
        self.h = h
        self.x = x
        self.eps = eps
        self.A = - 1 / 3
        self.B = 4 / 3

    def calc(self, h, x):
        res = self.A * ((func(x + h / 2) - func(x - h / 2)) / h) + self.B * (func(x + h) - func(x - h) / 2 * h)
        return res

    def runge(self):
        eps = self.eps
        h = self.h
        x = self.x
        while True:
            R = abs((self.calc(h, x) - self.calc(2 * h, x)) / 127)
            if R > eps:
                h /= 2

            if R <= eps:
                print(f'Достигнута нужна точность при h = {h}')
                print(f'Значение производной: {self.calc(h, x)}')
                print(f'Погрешность: {R}')
                break
        return 0


a = Derivative(1, 0.1, 10 ** -8)
a.runge()
