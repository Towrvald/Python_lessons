import numpy as np


# Этот алгоритм не учитывает нулевые элементы. Учёт и сортировка будет дополнена в 4 задании
class GaussElimin:
    def __init__(self, A, B):  # A- матрица при неизвестных, B- свободных членов
        self.A = A.copy()  # обязательно копируем, чтобы получить новый массив, а не ссылку на исходный
        self.B = B.copy()

    def trig(self):  # Зануляем все элементы ниже диагонали
        n = len(self.B)
        for string in range(0, n - 1):  # проходимся по всем диагональным элементам
            for next_string in range(string + 1, n):  # проходимся по всем строкам ниже текущего диагонального элемента
                if self.A[string, string] != 0:  # Если диагональный элемент не =0, то делим всю строку на этот элемент
                    x = self.A[string, string]
                    self.A[string, :] /= x
                    self.B[string] /= x

                self.A[string, :] *= self.A[next_string, string]  # умножаем строку на элемент под текущ.диаг.элементом
                self.B[string] *= self.A[next_string, string]
                self.A[next_string, :] -= self.A[string, :]
                self.B[next_string] -= self.B[string]
        return self.A

    def inverse_trig(self):  # тот же алгоритм, но в обратную сторону, чтобы занулить верхний треугольник
        n = len(self.B)
        for string in range(n - 1, 0, -1):
            for next_string in range(string - 1, -1, -1):
                if self.A[string, string] != 0:
                    x = self.A[string, string] / self.A[next_string, string]
                    self.A[next_string, :] *= x
                    self.B[next_string] *= x

                self.A[next_string, :] -= self.A[string, :]
                self.B[next_string] -= self.B[string]
                self.A[next_string, :] /= x  # чтобы оставить диагональный член без изменений
                self.B[next_string] /= x
        return self.A

    def calc_diag(self):
        self.trig()
        self.inverse_trig()
        return 0

    def answer(self):  # Выводим ответ
        self.calc_diag()
        n = len(self.B)
        for element in range(n):  # Делим столбец B на значение диагональных элементов
            self.B[element] /= self.A[element, element]
        return self.B


A = np.array([[2.0, -3.0, -1.0], [3.0, 2.0, -5.0], [2.0, 4.0, 1.0]], dtype=float)
B = np.array([3.0, -9.0, -5.0], dtype=float)
x = GaussElimin(A, B)
print(x.answer())
