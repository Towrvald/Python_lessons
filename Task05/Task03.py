import numpy as np


class GaussElimin:
    def __init__(self, A, B):
        self.A = A.copy()
        self.B = B.copy()

    def trig(self):
        n = len(self.B)
        for string in range(0, n - 1):
            for next_string in range(string + 1, n):
                if self.A[string, string] != 0:
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
                if self.A[string, string] != 0:
                    x = self.A[string, string] / self.A[next_string, string]
                    self.A[next_string, :] *= x
                    self.B[next_string] *= x

                self.A[next_string, :] -= self.A[string, :]
                self.B[next_string] -= self.B[string]
                self.A[next_string, :] /= x
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


A = np.array([[6, -4, 1],
              [-4, 6, -4],
              [1, -4, 6]], dtype=float)

B1 = np.array([-14, 36, 6], dtype=float)
B2 = np.array([22, -18, 7], dtype=float)
x = GaussElimin(A, B1)
y = GaussElimin(A, B2)
np.set_printoptions(suppress=True)
print(f'x1   x2   x3')
print(x.answer())
print(y.answer())
