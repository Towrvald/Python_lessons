from math import *
import numpy as np


class Solve:
    def __init__(self):
        self.mean = np.array([[9, 10, 11], [54.80, 54.06, 53.34], [65.59, 64.59, 63.62]])
        self.mean[1] = np.radians(self.mean[1])
        self.mean[2] = np.radians(self.mean[2])

    def calc_x(self, a, b):
        return 500 * (tan(b) / (tan(b) - tan(a)))

    def calc_y(self, a, b):
        return 500 * (tan(a) * tan(b) / (tan(b) - tan(a)))

    def calculate_velocity(self):
        vx = (self.calc_x(self.mean[1][2], self.mean[2][2]) - self.calc_x(self.mean[1][0], self.mean[2][0])) / (
                self.mean[0, 2] - self.mean[0][0])
        vy = (self.calc_y(self.mean[1][2], self.mean[2][2]) - self.calc_y(self.mean[1][0], self.mean[2][0])) / (
                self.mean[0, 2] - self.mean[0][0])
        angle = degrees(atan(vy / vx))

        print("Скорость по X:", round(vx, 2), 'м/c')
        print("Скорость по Y:", round(vy, 2), 'м/c')
        print("Модуль скорости:", round(sqrt(vy ** 2 + vx ** 2), 2), 'м/c')
        print("Угол наклона:", round(angle, 2), 'градусов')


x = Solve()
x.calculate_velocity()
