# Модуль - остальное
# Функции для обработки различных типов данных
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


# Функции для обработки словарей
def add_to_dict(some_dict, some_key, some_value):
    if (type(some_dict) == dict and type(some_key) == int):
        some_dict[some_key] = some_value
        return some_dict
    else:
        return ("Ошибка в типе данных параметра. Параметр - словарь")

def sum_dict (some_dict1, some_dict2, some_dict3):
    if (type(some_dict1) == dict and type(some_dict2) == dict and type(some_dict3) == dict):
        some_dict4 = some_dict1.copy()
        some_dict4.update(some_dict2)
        some_dict4.update(some_dict3)
        return some_dict4
    else:
        return ("Ошибка в типе данных параметров. Параметры - словари")

def del_of_dict(some_dict, some_key):
    if (type(some_dict) == dict and type(some_key) == int):
        del some_dict[some_key]
        return some_dict
    else:
        return ("Ошибка в типе данных параметров. Параметры - словарь и ключ")

def key_in_dict (some_dict, some_key):
     if (type(some_dict) == dict and type(some_key) == int):
        if some_key in some_dict:
             return True
        else:
            return False
     else:
        return ("Ошибка в типе данных параметров. Параметры - словарь и ключ")

# Функции для обработки множеств
def del_of_set(some_set, some_value):
  if(type(some_set) == set):
      if some_value in some_set: 
         some_set.remove(some_value)
         return some_set
      else:
        return False
  else:
    return ("Ошибка в типе данных параметра. Параметр - множество")

def custom_len_of_set(some_set, choice):
    if (type(some_set) == set and choice == 1):
        return (len(some_set))
    elif (type(some_set) and choice == 2):
        counter = 0
        for i in some_set:
            counter += 1
        return counter
    else:
        return ("Ошибка в типе данных параметра. Параметр - множество")

def check_value_in_set(some_set, some_value):
    if (type(some_set) == set):
        if some_value in some_set:
            return True
        else:
            return False
    else:
        return ("Ошибка в типе данных параметра. Параметр - множество")

# Функции для обработки кортежей
def add_set(some_tuple, some_value):
    if (type(some_tuple) == tuple):
        some_list = list(some_tuple)
        some_list.append(some_value)
        some_tuple = set(some_list)
        return some_tuple
    else:
        return ("Ошибка в типе данных параметра. Параметр - кортеж")

def count_tuple(some_list):
    if(type(some_list) == list):
        counter = 0
        for k in list1:
            if isinstance(k, tuple):
                counter += 1
        return counter
    else:
        return ("Ошибка в типе данных параметра. Параметр - кортеж")

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

