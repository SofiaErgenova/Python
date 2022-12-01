# 1- Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def Сreate_random_list(len_list: int,first_num: int, second_num: int) -> (list):
    """функция задает список из случайных чисел"""
    from random import randint
    newlist = []
    for i in range(len_list):
        newlist.append(randint(first_num, second_num))
    return newlist

def Сount_sum_odd_index(numbers: list):
    """функция считает сумму элементов на нечетной позиции"""
    numbers = numbers[1::2]
    sum = 0
    for i in numbers:
         sum = sum + i
    print(f"ответ: {sum}")    

# newnumbers = Сreate_random_list(5,0,10)
# print(newnumbers)

# Сount_sum_odd_index(newnumbers)


# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def search_product_multiplication(numbers:list) -> list:
    """поиск произведения пар чисел списка"""

    multi_numbers = []

    if len(numbers)%2 == 1:
        len_multi_numbers = int(len(numbers)/2) + 1
    else:
        len_multi_numbers = int(len(numbers)/2)

    for i in range(len_multi_numbers):
        multi_numbers.append(numbers[i] * numbers[-i-1])
    print(multi_numbers)
    return(multi_numbers)

# task_numbers = Сreate_random_list(5,0,10)
# print(task_numbers)

# search_product_multiplication(task_numbers)

# 3-Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

def Сreate_random_float_list(len_list: int, num_round: int, first_num: float, second_num: float) -> (list):
    """функция задает список из случайых вещественных чисел"""
    import random
    float_list = []
    for i in range(len_list):
        x = round(random.uniform(first_num, second_num),num_round)
        float_list.append(x)
    print(float_list)
    return float_list

float_list_task = Сreate_random_float_list(5,2,1,10)


def Search_fractional_part_number(test_number:list, num_round: int) -> list:
    fractional_part_number = []

    for i in range(len(float_list_task)):
        while float_list_task[i] >= 1:
            float_list_task[i] = round((test_number[i] - 1), num_round)
        else:
            fractional_part_number.append(float_list_task[i])
    print(fractional_part_number)
    return fractional_part_number

float_list_task = Search_fractional_part_number(float_list_task,2)

def Search_max_min_diff(test_numbers:list) -> float:
    """нахождение максимального, минимального значения и их разницы"""
    max = test_numbers[0]
    min = test_numbers[0]
    for i in range(len(test_numbers)):
        if test_numbers[i] > max:
            max = test_numbers[i]
        elif test_numbers[i] < min:
            min = test_numbers[i]
    diff = round((max - min),3)
    print(f"минимальное значение {min}, максимальное значение {max}, разница {diff}")
    return min, max, diff

Search_max_min_diff(float_list_task)



# 4- Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


# 5-Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# Негафибоначчи






