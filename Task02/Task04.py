from math import *


class Function:
    @staticmethod
    def exp(x):
        return exp(x)


class Derivative:
    def __init__(self, f, x, h, A, B, C):
        self.f = f
        self.x = x
        self.h = h
        self.A = A
        self.B = B
        self.C = C

    def calculate_difference(self):
        return (self.A * self.f(self.x + 2 * self.h) + self.B * self.f(self.x + self.h) + self.C * self.f(
            self.x) + self.B * self.f(self.x - self.h) + self.A * self.f(self.x - 2 * self.h)) / self.h ** 2


func = Function()
diff = Derivative(func.exp, 1, 0.1, -(1 / 12), 16 / 12, -30 / 12)
true_value = func.exp(1)

for _ in range(10):
    print('h =', diff.h, 'error =', abs(true_value - diff.calculate_difference()))
    diff.h /= 10
