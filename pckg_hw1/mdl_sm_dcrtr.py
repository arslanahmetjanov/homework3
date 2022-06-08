# Декораторы для обработки различных типов данных
def squaring_decorator(function):
    def wrapper(a, b, c):
        func = function(a, b, c)
        make_squaring = func ** 2
        return make_squaring
    return wrapper

@squaring_decorator
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

def uppercase_decorator(function):
    def wrapper(some_str):
        func = function(some_str)
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
    
@uppercase_decorator
def custom_invert_str(some_str):
    if (type(some_str) == str):
        return some_str[::-1]
    else:
        return "Ошибка в типе данных параметра. Параметр - строка"

