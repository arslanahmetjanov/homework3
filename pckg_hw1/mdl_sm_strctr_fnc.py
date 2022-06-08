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




