# 1 - Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def Compose_simple_multipliers_list(num: int)-> list:
    """составление списка простых множителей числа"""

    simple_multipliers_list = []

    divider = 2
    while num > 1:
        if num % divider == 0:
            num = num/divider
            simple_multipliers_list.append(divider)
        else:    
            divider = divider + 1
    
    else:
        print(simple_multipliers_list)
        return simple_multipliers_list

# n = int(input("Введите число: "))
# Compose_simple_multipliers_list(n)


# 2 - Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

def Сreate_random_list(len_list: int,first_num: int, second_num: int) -> (list):
    """функция задает список из случайных чисел"""
    from random import randint
    newlist = []
    for i in range(len_list):
        newlist.append(randint(first_num, second_num))
    return newlist

def Delete_repeats (list_with_repeats: list) -> list:
    """удаление повторов в списке"""

    list_without_repeats = []
    for i in range(len(list_with_repeats)):
        if list_with_repeats[i] not in list_without_repeats:
            list_without_repeats.append(list_with_repeats[i])
            
    print(list_without_repeats)
    return list_without_repeats

# repeats = Сreate_random_list(10,1,10)
# print(repeats)
# Delete_repeats(repeats)


# 3 - В файле, содержащем фамилии студентов и их оценки, 
# изменить на буквы в верхнем регистре тех студентов, 
# которые имеют средний балл более «4».
# Нужно перезаписать файл. 
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4
# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4


# lines = ["Ангела Меркель 5", "Энакин Скайуокер 5", "Фредди Меркури 3","Александр Пушкин 4"]
# with open('file_2.txt','w') as data:
#     for  line in lines:
#         data.write(line + '\n')

# file = open('file_2.txt', 'r')
# file = file.read()
# print(file)
# data.close()

# with open('file_2.txt','w') as data:
#     for line in lines:
#             if line.find('5') != -1:
#                 line = line.upper()
#                 data.write(line + '\n')
#             else:
#                 data.write(line + '\n')

# file = open('file_2.txt', 'r')
# file = file.read()
# print(file)
# data.close()


# 4- Шифр Цезаря - это способ шифрования, где каждая буква 
# смещается на определенное количество символов влево или вправо.
#  При расшифровке происходит обратная операция. 
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
#  "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

def Caesar_cipher(word: str, key_cipher: int) -> str:
    """шифр Цезаря"""

    alfabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    cipher = ''

    for letter in word:
            letter_index = alfabet.find(letter)
            new_index = (letter_index + key_cipher)%33
            cipher = cipher + alfabet[new_index]
      
    print(f"шифр: {cipher}")
    return cipher


def Caesar_cipher_decoding(cipher: str, key_cipher: int) -> str:
    """Расшифровка шифра Цезаря"""
    
    alfabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    decoding = ''

    for letter in cipher:
        letter_index = alfabet.find(letter)
        new_index = (letter_index - key_cipher)%33
        decoding = decoding + alfabet[new_index]
     
    print(f"расшифровка: {decoding}")
    return decoding

# test_word = input("Введите слово для зашифровки на кириллице: ")
# key = int(input("Введите ключ шифрования: "))

# test_cipher = Caesar_cipher(test_word,key)
# Caesar_cipher_decoding(test_cipher,key)


# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл

def Write_text_file (path: str, lines: str ):
    """запись в файл"""
    with open(path,'w') as data:
        for  line in lines:
            data.write(line)
    return path

def Read_text_file (path: str):
    """чтение файла"""
    data = open(path,'r')
    for line in data:
        print(line)
    data.close()
    return line

def Make_RLE_algoritm (line: str) -> str:
    """RLE алгоритм: модуль сжатия"""

    cipher = ''
    count = 1 
    i = 0
    
    while i < len(line)-1: 
        if line[i] == line[i+1]:
            count = count + 1
            i += 1 
        else:
            if count == 1:
                 cipher = cipher + line[i]
            else:
                cipher = cipher + str(count) + line[i]
            count = 1
            i +=1 
    if count == 1:
        cipher = cipher + line[i]
    else: 
        cipher = cipher + str(count) + line[i]

    print(f"шифр: {cipher}")
    return cipher

def RLE_algoritm_decoding (cipher: str) -> str:
    """RLE алгоритм: модуль восстановления""" 
    decoding = ''
    i = 0
    mult = ''

    for i in range(len(cipher)): 
        if cipher[i].isdigit():
            mult = mult + cipher[i] 
        else:
            if mult != '':
                decoding = decoding + int(mult)*cipher[i]
            else:
                decoding = decoding + cipher[i]
            mult = ''
    print(f"расшифровка: {decoding}")
    return decoding

line_1 = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
path_in = 'task_5_in.txt'

line_2 = '12A11B10C6D5E4FG python is s7o c7ol'
path_out = 'task_5_out.txt'

Write_text_file(path_in,line_1)

line_in = Read_text_file(path_in)

Make_RLE_algoritm(line_in)

line_out = Make_RLE_algoritm(line_in)

RLE_algoritm_decoding(line_out)

Write_text_file(path_out,line_out)

