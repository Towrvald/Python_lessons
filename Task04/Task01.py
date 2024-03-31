from math import *


# Как работает этот код:
# методом runge мы находим шаг h, при котором достигается нужная точность 10**-8, и фиксируем его
# метод calc считает интеграл квадратурой
# метод calc_recurrent считает интеграл рекуррентной формулой
# геттер выводит всё в консоль
# В конце выводится значение n, для которого ошибка сопоставима с интегралом


def func(x, n):
    return (1 / exp(1)) * (x ** n) * (exp(x))


class Integer:
    def __init__(self, h, a, b, n, eps):
        self.h = h
        self.a = a
        self.b = b
        self.eps = eps
        self.n = n

    def calc(self, h, n):  # интегрирование в диапазоне [a, b] с шагом h квадратурой
        sum = 0
        a = self.a
        b = self.b
        x = a + h
        while x < b:
            sum += (5 * func(x - h * sqrt(0.6) / 2, n) + 8 * func(x, n) + 5 * func(x + h * sqrt(0.6) / 2, n)) / 18
            x += h
        return h * sum

    def runge(self):  # Уменьшает h до тех пор, пока не достигнем нужной точности R
        eps = self.eps
        h = self.h
        n = self.n
        while True:
            R = abs((self.calc(h, n) - self.calc(2 * h, n)) / 127)
            if R > eps:
                h /= 2

            if R <= eps:
                print(f'Достигнута нужная точность при h = {h}')
                print(f'Значение интеграла: {self.calc(h, n)}')
                print(f'Погрешность: {R}')
                self.h = h  # фиксируме h на которой  достигнута нужная точность
                break
        return 0

    def calc_recurrent(self, n=0):  # интегрирование рекуррентной формулой
        if n == 0:
            return 1 - (1 / exp(1))
        else:
            return 1 - n * self.calc_recurrent(n - 1)

    def get_integer(self):
        n = self.n
        self.runge()  # вызываем, чтобы подобрать и зафиксировать h на нужную точность 10**-8
        h = self.h
        n_counter = 0  # Значение n, с которого ошибка сопоставима со значениме интеграла
        print('###############################\n')
        print('n     ', 'Квадратурой        ', 'Рекуррентной         ', 'Разница\n')
        while n <= 30:
            Gauss = self.calc(h, n)
            Recurrent = self.calc_recurrent(n)
            diff = abs(Gauss - Recurrent)
            if (
                    diff / Gauss * 100) >= 10:  # Сопоставим = одного порядка, следовательно, относ.погрешность не меньше 10%
                if n_counter == 0:
                    n_counter = n
                else:
                    pass
            print(f'{n}     {Gauss}     {Recurrent}     {diff}')
            n += 1
        print('Значение n, для которого ошибка сопоставима с интегралом: ', n_counter)
        return 0


a = Integer(0.1, 0, 1, 0, 10 ** -8)
a.get_integer()
