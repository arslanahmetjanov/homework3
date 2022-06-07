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
