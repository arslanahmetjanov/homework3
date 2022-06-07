def average_count(some_structure):
    if (type(some_structure) == list or type(some_structure) == set or type(some_structure) == tuple):
        rslt = sum(some_structure) / len(some_structure)
        return rslt
    elif (type(some_structure) == dict):
        counter_sum = 0
        for i in some_structure:
            counter_sum += some_structure[i]
        rslt = counter_sum / len(some_structure)
        return rslt
    else:
        return("Ошибка в типах данных параметров. Параметр может быть списком, множеством, кортежом или словарем")

def max(a, b, c):
    if (type(a) == int and type(b) == int and type(c) == int):
        if (a >= b and a >= c):
            return a
        elif (b >= a and b >= c):
            return b
        elif (c >= a and c >= b):
            return c
    else:
        return "Ошибка в типах данных параметров. Параметры - цифры в виде (1, 2, 3)"

def custom_invert_str(some_str):
    if (type(some_str) == str):
        return some_str[::-1]
    else:
        return "Ошибка в типе данных параметра. Параметр - строка"

def factorial_count(n):
    if (type(n) == int and n > 0):
        if n == 1:
            return 1
        return factorial_count(n - 1) * n
    else:
        return "Ошибка в типе данных параметра. Параметр - число"

def unique_list(l):
    if (type(l) == list):
        t = [] 
        t = list(set(l))
    else:
        return "Ошибка в типе данных параметра. Параметр - список"

def check_palindrom(s1): 
    if (type(s1) == str):
        f = lambda s: s[::-1]
        s2 = f(s1)
        if s1 == s2:
            return True
        else:
            return False
    else:
        return "Ошибка в типе данных параметра. Параметр - список"