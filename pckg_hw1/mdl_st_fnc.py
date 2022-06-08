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