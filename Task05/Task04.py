import numpy as np


class GaussElimin:
    def __init__(self, A, B):
        self.A = A.copy()
        self.B = B.copy()

    def sort(self):  # сортируем матрицу так, чтобы диагональные элементы !=0
        n = len(self.B)
        while True:
            for i in range(0, n - 1):  # меняем столбцы местами
                if self.A[i, i] == 0:
                    self.A[:, [i, i + 1]] = self.A[:, [i + 1, i]]

            for i in range(0, n - 1):  # меняем строки местами
                if self.A[i, i] == 0:
                    self.A[[i, i + 1], :] = self.A[[i + 1, i], :]
                    self.B[[i, i + 1]] = self.B[[i + 1, i]]

            if self.A[n - 1, n - 1] != 0:
                break
        return 0

    def trig(self):
        self.sort()
        n = len(self.B)
        for string in range(0, n - 1):
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


A = np.array([[2, 0, -1, 0],
              [0, 1, 2, 0],
              [-1, 2, 0, 1],
              [0, 0, 1, -2]], dtype=float)
B1 = np.array([1, 0, 0, 0], dtype=float)
B2 = np.array([0, 0, 1, 0], dtype=float)

x = GaussElimin(A, B1)
y = GaussElimin(A, B2)
print("    x1     x2      x3      x4")
print(x.answer())
print(y.answer())
