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