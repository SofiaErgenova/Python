#  1 Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
#  Пример:
#  Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
#  Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок


# test_str = input('Введите текст: ')
# find_str = input('Введите заданную строку: ')
# test_str = 'Пугать ты галок пугай'
# find_str = 'галок'

# with open('textIN_home_work_5.txt','w') as file:
#         file.write(test_str)

# with open('textIN_home_work_5.txt') as infile, open('textOUT.txt', "w") as outfile:
#     for line in infile:
#         line = line.split()
#         for i in range(len(line)):
#                if line[i].find(find_str) == -1:
#                     outfile.write(line[i] + " ")
               


# ; 2.Создайте программу для игры с конфетами человек против человека.
# ; Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета.
# ;  Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# ;  За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет.
# ;   Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# ; a) Добавьте игру против бота
# ; b) Подумайте как наделить бота ""интеллектом""
# ; Если делаете a и b - не нужно создавать отдельных файлов
# ;  с полностью копированным кодом, лучше выделите в отдельные функции бота и умного бота.


def Сreate_random_list(len_list: int,first_num: int, second_num: int) -> (list):
     """функция задает список из случайных чисел"""
     from random import randint
     newlist = []
     for i in range(len_list):
         newlist.append(randint(first_num, second_num))
     return newlist

# bonbon = int(input("Введите количество конфет: "))

# max_one_move = int(input("Введите максимальное количество конфет за один ход обоих игроков: "))
# print(f"Подсказка: сколько конфет взять в первый ход, чтобы победить: {bonbon % (max_one_move + 1)}")

# response = input("Хотите узнать, какой вы игрок? Нажмите enter")
# lot = Сreate_random_list(1,0,2)
# if lot[0] == 1:
#     print("Вы первый игрок!")
# else:
#     print("Вы второй игрок!")


# while bonbon >= 1:
#     move = int(input(f"Первый игрок, введите количество конфет от 1 до {max_one_move}: "))
#     bonbon = bonbon - move
#     print(f"Количество оставшихся конфет: {bonbon}")
#     if bonbon == 1:
#         print("Победитель - первый игрок")
#         break
    
#     move = int(input(f"Второй игрок, введите количество конфет от 1 до {max_one_move}: "))
#     bonbon = bonbon - move
#     print(f"Количество оставшихся конфет: {bonbon}")
#     if bonbon == 1:
#         print("Победитель - второй игрок")
#         break




#  3.Создайте программу для игры в ""Крестики-нолики"".

row_one = ['*' ,'*', '*']
row_two = ['*' ,'*', '*']
row_three = ['*' ,'*', '*']

print (''. join(row_one))
print(''. join(row_two))
print(''. join(row_three))


response = input("Кто ходит первым? Нажмите enter")
lot = Сreate_random_list(1,0,2)
if lot[0] == 1:
    print("Крестики!")
else:
    print("Нолики!")

count = 0 
while count <= 9:
        if lot[0] == 0:
                row = int(input("Ход ноликов.Введите номер ряда 1, 2 или 3: "))
                i = int(input("Введите номер позиции 0, 1 или 2: "))
                if row == 1 and lot[0] == 0:
                        row_one[i] = '0'
                        print (''. join(row_one))
                        print(''. join(row_two))
                        print(''. join(row_three))
                        
                        if (row_one[0] == row_two[1]== row_three[2]== '0' or
                        row_one[2] == row_two[1]== row_three[0]== '0' or
                        row_one[0] == row_two[0]== row_three[0]== '0' or
                        row_one[1] == row_two[1]== row_three[1]== '0' or
                        row_one[2] == row_two[2]== row_three[2]== '0' or
                        row_one[0] == row_one[1]== row_one[2]== '0' or
                        row_two[0] == row_two[1]== row_two[2]== '0' or
                        row_three[0] == row_three[1]== row_three[2]== '0'):
                                print("Победили нолики!")
                                break
                        count += 1
                        lot[0] == 1
                elif row == 2  and lot[0] == 0:
                        row_two[i] = '0'
                        print (''. join(row_one))
                        print(''. join(row_two))
                        print(''. join(row_three))
                        if (row_one[0] == row_two[1]== row_three[2]== '0' or
                        row_one[2] == row_two[1]== row_three[0]== '0' or
                        row_one[0] == row_two[0]== row_three[0]== '0' or
                        row_one[1] == row_two[1]== row_three[1]== '0' or
                        row_one[2] == row_two[2]== row_three[2]== '0' or
                        row_one[0] == row_one[1]== row_one[2]== '0' or
                        row_two[0] == row_two[1]== row_two[2]== '0' or
                        row_three[0] == row_three[1]== row_three[2]== '0'):
                                print("Победили нолики!")
                                break
                        count += 1
                        lot[0] == 1
                elif row == 3 and lot[0] == 0:
                        row_three[i] = '0'
                        print (''. join(row_one))
                        print(''. join(row_two))
                        print(''. join(row_three))
                        if (row_one[0] == row_two[1]== row_three[2]== '0' or
                        row_one[2] == row_two[1]== row_three[0]== '0' or
                        row_one[0] == row_two[0]== row_three[0]== '0' or
                        row_one[1] == row_two[1]== row_three[1]== '0' or
                        row_one[2] == row_two[2]== row_three[2]== '0' or
                        row_one[0] == row_one[1]== row_one[2]== '0' or
                        row_two[0] == row_two[1]== row_two[2]== '0' or
                        row_three[0] == row_three[1]== row_three[2]== '0'):
                                print("Победили нолики!")
                                break
                        count += 1
                        lot[0] == 1
                else:
                        print("Неверное значение")
        elif lot[0] == 1:
                row = int(input("Ход крестиков.Введите номер ряда 1, 2 или 3: "))
                i = int(input("Введите номер позиции 0, 1 или 2: "))
                if row == 1  and lot[0] == 1:
                        row_one[i] = '+'
                        print (''. join(row_one))
                        print(''. join(row_two))
                        print(''. join(row_three))
                        if (row_one[0] == row_two[1]== row_three[2]== '+' or
                        row_one[2] == row_two[1]== row_three[0]== '+' or
                        row_one[0] == row_two[0]== row_three[0]== '+' or
                        row_one[1] == row_two[1]== row_three[1]== '+' or
                        row_one[2] == row_two[2]== row_three[2]== '+' or
                        row_one[0] == row_one[1]== row_one[2]== '+' or
                        row_two[0] == row_two[1]== row_two[2]== '+' or
                        row_three[0] == row_three[1]== row_three[2]== '+'):
                                print("Победили крестики!")
                                break
                        count += 1
                        lot[0] == 0
                elif row == 2 and lot[0] == 1:
                        row_two[i] = '+'
                        print (''. join(row_one))
                        print(''. join(row_two))
                        print(''. join(row_three))
                        if (row_one[0] == row_two[1]== row_three[2]== '+' or
                        row_one[2] == row_two[1]== row_three[0]== '+' or
                        row_one[0] == row_two[0]== row_three[0]== '+' or
                        row_one[1] == row_two[1]== row_three[1]== '+' or
                        row_one[2] == row_two[2]== row_three[2]== '+' or
                        row_one[0] == row_one[1]== row_one[2]== '+' or
                        row_two[0] == row_two[1]== row_two[2]== '+' or
                        row_three[0] == row_three[1]== row_three[2]== '+'):
                                print("Победили крестики!")
                                break
                        count += 1
                        lot[0] == 0
                elif row == 3 and lot[0] == 1:
                        row_three[i] = '+'
                        print (''. join(row_one))
                        print(''. join(row_two))
                        print(''. join(row_three))
                        if (row_one[0] == row_two[1]== row_three[2]== '+' or
                        row_one[2] == row_two[1]== row_three[0]== '+' or
                        row_one[0] == row_two[0]== row_three[0]== '+' or
                        row_one[1] == row_two[1]== row_three[1]== '+' or
                        row_one[2] == row_two[2]== row_three[2]== '+' or
                        row_one[0] == row_one[1]== row_one[2]== '+' or
                        row_two[0] == row_two[1]== row_two[2]== '+' or
                        row_three[0] == row_three[1]== row_three[2]== '+'):
                                print("Победили крестики!")
                                break
                        count += 1
                        lot[0] == 0
                else:
                        print("Неверное значение")
else:
        print("Ничья")
        