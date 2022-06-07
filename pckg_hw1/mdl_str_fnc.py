def choise_len_for_str(some_str, choice):
    if (type(some_str) == str and (choice == 1 or choice == 2 )):
        if choice == 1:
            return len(some_str)
        elif choice == 2:
            counter = 0
            for i in some_str:
                counter += 1
            return counter
    else:
        return("Ошибка в типах данных параметров. Первый - строка, второй - цифры: 1 или 2")


def change_dollar_for_str(str1, str2):
    if (type(str1) == str and type(str2) == str):
        dollar = "$"
        return str1.replace(str2, dollar)

    else:
        return("Ошибка в типах данных параметров. Первый - главная строка, второй - подстрока для замены")

def final_plus_end_for_str(some_str):
    if (type(some_str) == str):
        length = len(some_str)
        if length >=2:
            new_str = some_str[0] + some_str[1] + some_str[length - 2] + some_str[length - 1]
            return new_str
        else:
            return " "
    else:
        return("Ошибка в типе данных параметра. Параметр - строка")

def invert_str(some_str):
    if (type(some_str) == str):
        some_str = some_str[::-1]
        return "".join(some_str)
    else:
        return("Ошибка в типе данных параметра. Параметр - строка")

def index_for_str(some_str):
    if (type(some_str) == str):
        length = len(some_str)
        for i in range(length):
            return i, "-", some_str[i]
    else:
        return("Ошибка в типе данных параметра. Параметр - строка")

def change_register_str(some_str):
    if (type(some_str) == str):
        if some_str.isupper():
            return some_str.lower()
        else:
            return some_str.upper()
    else:
        return("Ошибка в типе данных параметра. Параметр - строка")

def find_count_of_item_in_str(some_str):
    if (type(some_str) == str):
        length_str = len(some_str)
        item_max = ""
        counter_max = 0
        for i in range(length_str):
            item = some_str[i]
            counter = 0
            for i in some_str:
                if i == item:
                    counter += 1
            if counter > counter_max:
                counter_max = counter
                item_max = item
        return f"{item_max} встречается чаще всего, а именно {counter_max} раз(-а)"
    else:
        return("Ошибка в типах данных параметров. Параметр - строка")