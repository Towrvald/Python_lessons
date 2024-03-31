import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class GaussElimin:
    def __init__(self, A, B):
        self.A = A.copy()
        self.B = B.copy()

    def trig(self):
        n = len(self.B)
        for string in range(n - 1):
            for next_string in range(string + 1, n):
                if self.A[next_string, string] != 0:
                    x = self.A[string, string]
                    self.A[string, :] /= x
                    self.B[string] /= x
                    self.A[string, :] *= self.A[next_string, string]
                    self.B[string] *= self.A[next_string, string]
                    self.A[next_string, :] -= self.A[string, :]
                    self.B[next_string] -= self.B[string]
        return self.A

    def inverse_trig(self):
        n = len(self.B)
        for string in range(n - 1, 0, -1):
            for next_string in range(string - 1, -1, -1):
                if self.A[next_string, string] != 0:
                    x = self.A[string, string] / self.A[next_string, string]
                    self.A[next_string, :] *= x
                    self.B[next_string] *= x
                    self.A[next_string, :] -= self.A[string, :]
                    self.B[next_string] -= self.B[string]
                    self.A[next_string, :] /= x
                    if self.B[next_string] != 0:
                        self.B[next_string] /= x
        return self.A

    def calc_diag(self):
        self.trig()
        self.inverse_trig()
        return 0

    def answer(self):
        self.calc_diag()
        n = len(self.B)
        for element in range(n):
            self.B[element] /= self.A[element, element]

        return self.B


def r(t, g, theta):
    r0 = 100
    a = np.array([[1, 0, 0, 10], [-1, 1, 0, 4], [0, -1, 1, 5], [0, 0, -1, 6]])
    b = np.array([10 * g * (np.sin(theta) - 0.25 * np.cos(theta)),
                  4 * g * (np.sin(theta) - 0.3 * np.cos(theta)),
                  5 * g * (np.sin(theta) - 0.2 * np.cos(theta)), -6 * g])
    T = np.linalg.solve(a, b)
    return r0 + T[3] * t ** 2 / 2


def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(100, r(10, g, theta))
    return line,


def animate(t):
    x = np.linspace(0, t, t + 1)
    y = np.array([r(i, g, theta) for i in range(t + 1)])
    line.set_data(x, y)
    return line,


g = 9.82
theta = np.pi / 4

a = np.array([[1, 0, 0, 10], [-1, 1, 0, 4], [0, -1, 1, 5], [0, 0, -1, 6]], dtype=float)
b = np.array([10 * g * (np.sin(theta) - 0.25 * np.cos(theta)),
              4 * g * (np.sin(theta) - 0.3 * np.cos(theta)),
              5 * g * (np.sin(theta) - 0.2 * np.cos(theta)), -6 * g], dtype=float)

T = GaussElimin(a, b)
print(T.answer())

fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-', color='black', markerfacecolor='red')

ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)

plt.xlabel('Time')
plt.ylabel('Position')

plt.show()
