# 1 - Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

# str = input("Введите число: ")
# str_notdot = str.replace('.','')
# str_notdash= str_notdot.replace('-','')

# summa = 0
# for i in str_notdash:
#     summa = summa + int(i)
# print(summa)


# 2 - Напишите программу, которая принимает на вход число N 
# и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите число: "))
# factorial = 1
# list = []
# for i in range(1,n+1):
#     factorial = factorial*i
#     list.append(factorial)
# print(list)

    
# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте
# элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

# N = int(input("Введите размер массива: "))

# from random import randint
# numbers = []
# Nneg = 0
# for i in range(N):
#     numbers.append(randint(-10, 10))
#     if numbers[i] < 0:
#         Nneg = Nneg + 1
# print(numbers)

# for i in range(N + Nneg):
#     if numbers[i] < 0:
#         numbers.insert(i+1, 0)
# print(numbers)



# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. 
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, 
# остальные получили по две монеты. Далее человек, на котором остановился счет, 
# отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. 
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. 
# Составьте алгоритм, который проводит эту игру. 
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep. 
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.

n = int(input("Введите количество человек n: "))
m = int(input("Введите количество отсчитываемых человек m: "))

list_money = []
for i in range(n):
    list_money.append(0)       

peoples = list(range(0,n))

while n > 1:
    for i in range(n):
        if i < m:
            list_money[i] = list_money[i]+1
        else:
            list_money[i] = list_money[i]+2  
         
    m = m % n  
    list_money[m] = list_money[m] + list_money[m-1]  
    del peoples[m-1]
    del list_money[m-1]
    n = n-1

    peoples_1 = peoples[m-1:]
    peoples_2 = peoples[0:m-1]
    peoples = peoples_1 + peoples_2
    
    list_money_1 = list_money[m-1:]
    list_money_2 = list_money[0:m-1]
    list_money = list_money_1 + list_money_2

    print(f"Номера оставшихся в круге: {peoples}")
    print(f"Количество их монет: {list_money}")

    str = input("Продолжаем игру? Введите да или нет: ")
    if str == "да":
        continue
    elif str == "нет":
        break
    else:
        print("невалидный ответ")

    
else:
    print(f"Номер последнего человека {peoples}")
    print(f"Количество его монет: {list_money}")