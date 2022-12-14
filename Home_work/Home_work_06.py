
# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate,
#  list comprehension

# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


# data = input("Введите список: ")
# search_object = input("ВВедите искомый элемент:")

# search_indexes = [index for index, element in enumerate(data) if element == search_object]
# print(search_indexes)

# if len(search_indexes) < 2:
#     print('-1')
# else:
#     print(search_indexes[1])


# 2- Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# import random
# numbers = [random.randint(1,10) for i in range (6)]
# print(numbers)

# first_half_list = [element for index, element in enumerate(numbers) if index < len(numbers)/2]

# sec_half_list = [element for index, element in enumerate(numbers) if index > (len(numbers)/2 - 1)]

# sec_half_list.reverse()

# mult_numbers = list(map(lambda first_half_el, sec_half_el: first_half_el*sec_half_el, first_half_list, sec_half_list))
# print(mult_numbers)

  
# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = 5
list_three = list((map(lambda i: (-3)**i,[i for i in range(0,n)])))
print(list_three)


# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.

# https://gb.ru/lessons/284810
# http://lassieshops.ru/index.php?route=product/category&path=61_62_75&page=6
# https://uchi.ru/marathons/students/progresses/


# url_str = "https://gb.ru/lessons/284810"

# index_start = url_str.find('/')
# index_end = url_str.find('/',index_start+2)
# list_url_str = list(url_str)

# domen = [element for index,element in enumerate(list_url_str) if index > index_start+1 and index < index_end]
# print(''.join(domen))



# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.

# import random
# numbers = [random.randint(1,100) for i in range (200)]

# new_num = [(index, element) for index, element in enumerate(numbers) if index != element]

# print(new_num)
# print(len(new_num))

# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]


# sum_tuple_multiple_five = [(index, element) for index, element in new_num if (index + element)% 5 == 0]

# print(sum_tuple_multiple_five)






