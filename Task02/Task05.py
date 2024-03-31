import numpy as np
import matplotlib.pyplot as plt


class Simulation:
    def __init__(self):
        self.R = 0.09
        self.V = 2 * np.pi * 5000.0 / 60
        self.theta = 0.0
        self.x = []
        self.y = []

    def position(self, theta):
        return 0.09 * (np.cos(theta) + np.sqrt(2.5 ** 2 - np.sin(theta) ** 2))

    def derivative(self, func, a, h):
        return (func(a + h) - 2 * func(a) + func(a - h)) / h ** 2

    def simulate_motion(self):
        print("Угол", "     ", "ускорение")
        for i in range(37):
            self.x.append(self.theta * 360 / (2 * np.pi))
            print(round(360 * self.theta / (2 * np.pi), 1), "\t",
                  round(self.derivative(self.position, self.theta, 1e-6) * self.V ** 2, 1))
            self.y.append(self.derivative(self.position, self.theta, 1e-6) * self.V ** 2)
            self.theta += 2 * np.pi * 5 / 360

    def plot_motion(self):
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y)
        plt.xlabel("Угол, град.")
        plt.ylabel("Ускорение, м/с^2")
        plt.show()


x = Simulation()
x.simulate_motion()
x.plot_motion()
