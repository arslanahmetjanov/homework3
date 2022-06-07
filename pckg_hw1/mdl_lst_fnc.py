def sum_for_list(some_list, choice):
    if (type(some_list) == list and type(choice) == int and choice == 1):
        return (sum(some_list))
    elif (type(some_list) == list and type(choice) == int and choice == 2):
        x = 0
        for i in some_list:
            x = x + i
        return x
    else:
        return("Ошибка в типе данных параметра. Параметр - список чисел")

def multyply_of_list(some_list, num):
    if  (type(some_list) == list and type(num) == int):
        for i in range(len(some_list)):
            some_list[i] *= num
        return some_list
    else:
        return("Ошибка в типе данных параметра. Параметр - список чисел")

def custom_concatenation(some_list1, some_list2, choice):
    if (type(some_list1) == list and type(some_list2) == list and choice == 1):
        return some_list1 + some_list2
    elif (type(some_list1) == list and type(some_list2) == list and choice == 2):
        for i in some_list2:
            some_list1.append(i)
        return some_list1
    elif (type(some_list1) == list and type(some_list2) == list and choice == 3):
        some_list1.extend(some_list2)
        return some_list1
    else:
        return ("Ошибка в типе данных параметров. Параметры - списки")

def change_index(some_list):
    if (type(some_list) == list):
        end_list = some_list[len(some_list)-1]
        some_list.insert(0, end_list)
        some_list.pop()
        return some_list
    else:
        return ("Ошибка в типе данных параметра. Параметр - список")

def in_one_number (some_list):
    if (type(some_list) == list):
        convert_list = ''.join(map(str,some_list))
        convert_list = int(convert_list)
        return convert_list
    else:
        return ("Ошибка в типе данных параметра. Параметр - список чисел")

def del_double_of_list(some_list):
    if(type(some_list) == list):
        original_list = list(set(some_list))
        return original_list
    else:
        return ("Ошибка в типе данных параметра. Параметр - список")