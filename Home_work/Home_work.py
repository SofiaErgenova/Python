# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит
# в нужный диапазон
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

# number = int (input('Введите цифру от 1 до 7:  '))

# if number > 7 or number <= 0 :
#     print("неверное значение")
# elif number >=1 and number <=5:
#     print("Это рабочий день")
# elif number==6 or number == 7:
#     print("Это выходной день")


# 2- Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
# Нужно написать таблицу истинности.

def truth_test(one,two,three):
    print(f'для {one},{two},{three}')
    if not(one or two or three) == (not one and not two and not three):
        print('это истина')
    else:
        print('это ложь')
        
truth_test(0,0,0)
truth_test(0,0,1)
truth_test(0,1,0)
truth_test(1,0,0)
truth_test(0,1,1)
truth_test(1,0,1)
truth_test(1,1,0)
truth_test(1,1,1)

# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
#и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3 
    
# coord_x = int(input('Введите координату х:  '))
# coord_y = int(input('Введите координату у:  '))

# if coord_x == 0 or coord_y == 0:
#     print("x и у не должны равняться нулю")
# elif coord_x > 0 and coord_y > 0:
#     print("это первая четверть")
# elif coord_x < 0 and coord_y > 0:
#     print("это вторая четверть")
# elif coord_x < 0 and coord_y < 0:
#     print("это третья четверть")
# elif coord_x > 0 and coord_y < 0:
#     print("это четвертая четверть")

# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# Пример:
# - quarter = 1 => x∈(0, ∞) u y∈(0,∞)

# quarter = int(input('Введите номер четверти от 1 до 4:  '))

# if quarter < 1 or quarter > 4:
#     print("неверное значение")
# elif quarter == 1:
#     print("x∈(0, ∞) u y∈(0,∞)")
# elif quarter == 2:
#     print("x∈(-∞,0) u y∈(0,∞)")
# elif quarter == 3:
#     print("x∈(-∞,0) u y∈(-∞,0)")
# elif quarter == 4:
#     print("x∈(0, ∞) u y∈(-∞,0)")

# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5.09
# A (7,-5); B (1,-1) -> 7.21


# coord_first_x = float(input('Введите координату х точки A:  '))
# coord_first_y = float(input('Введите координату y точки A:  '))
# coord_second_x = float(input('Введите координату x точки B:  '))
# coord_second_y = float(input('Введите координату у точки B:  '))

# import math
# print(round(math.sqrt(((coord_second_y - coord_first_y)**2 + (coord_second_x - coord_first_x)**2)),2))
