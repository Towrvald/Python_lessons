import numpy as np

#Здесь по вашему примеру, поэтому без описания
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


a = np.array([[2.0, -3.0, -1.0], [3.0, 2.0, -5.0], [2.0, 4.0, 1.0]])
b = np.array([3.0, -9.0, -5.0])

lu_decomp = LUDecomposition(a)
lu_solved = LUSolver(lu_decomp.decompose(), b)
print(lu_solved.solve())
