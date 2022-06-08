# Функции для обработки чисел
def max_count(a, b, c):
    if (type(a) == int and type(b) == int and type(c) == int):
        if (a >= b and a >= c):
            return a
        elif (b >= a and b >= c):
            return b
        elif (c >= a and c >= b):
            return c
    else:
        return "Ошибка в типах данных параметров. Параметры - цифры в виде (1, 2, 3)"


def factorial_count(n):
    if (type(n) == int and n > 0):
        if n == 1:
            return 1
        return factorial_count(n - 1) * n
    else:
        return "Ошибка в типе данных параметра. Параметр - число"
