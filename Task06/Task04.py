import numpy as np


# Здесь сортировку добавил, которую в предыдущем занятии реализовывал
class LUDecomposition:
    def __init__(self, a):
        self.a = a
        self.n = len(a)

    def decompose(self):
        for i in range(self.n - 1):
            for k in range(i + 1, self.n):
                if self.a[i][i] != 0:
                    x = self.a[k][i] / self.a[i][i]
                else:
                    x = 0
                for j in range(i, self.n):
                    self.a[k][j] -= x * self.a[i][j]
                self.a[k][i] = x
        return self.a


class LUSolver:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n = len(a)

    def solve(self):
        for k in range(1, self.n):
            for j in range(k):
                self.b[k] -= np.dot(self.a[k][j], self.b[j])
        self.b[self.n - 1] /= self.a[self.n - 1][self.n - 1]

        for k in range(self.n - 2, -1, -1):
            self.b[k] = (self.b[k] - np.dot(self.a[k][k + 1:], self.b[k + 1:])) / self.a[k][k]
        return self.b


def sort(a, b):
    n = len(a)
    while True:
        for i in range(0, n - 1):
            if a[i, i] == 0:
                a[:, [i, i + 1]] = a[:, [i + 1, i]]

        for i in range(0, n - 1):
            if a[i, i] == 0:
                a[[i, i + 1], :] = a[[i + 1, i], :]
                b[[i, i + 1]] = b[[i + 1, i]]

        if a[n - 1, n - 1] != 0:
            break
    return a, b


a = np.array([[0, 0, 2, 1, 2],
              [0, 1, 0, 2, -1],
              [1, 2, 0, -2, 0],
              [0, 0, 0, -1, 1],
              [0, 1, -1, 1, -1]], dtype=float)

b = np.array([1, 1, -4, -2, -1], dtype=float)
a, b = sort(a, b)
lu_decomp = LUDecomposition(a)
lu_solved = LUSolver(lu_decomp.decompose(), b)
np.set_printoptions(suppress=True)
print(lu_solved.solve())
