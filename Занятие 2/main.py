# Максим Игоревич

# Задача 1
# у васи X друзей, каждому он купил по 3 куска пиццы по 80 руб
# и тортик один на всех за 700
# сколько денег съел каждый друг?

# x = input('Сколько друзей? ')
# x = int(x)
# pizza = 240
# tortik = 700
# otvet = tortik/(x+1) + pizza
# print(otvet)

# x = int( input('Сколько друзей? '))
# print(700/(x+1) + 240)

# Задача 2
# Пользователь вводит число n. С начала суток прошло n минут.
# Определите, сколько часов и минут будут показывать электронные часы в этот момент.

# примеры 1000 -> 16 40        500 -> 8 20

# x = int( input())
# a = x//60
# b = x%60
# print (a,b)


# Задача 3
# Пользователь вводит число n - количество секунд.
# Определите, сколько часов и минут и секунд будут показывать электронные часы в этот момент.

# примеры 3750 -> 1 час 2 мин 30 сек
# 1:2:30

# n = int( input())
# a = n//3600
# b=n%3600//60
# c = n%60
# print(a,b, c)

# Задача 4
# Напишите программу, которая считывает значения двух переменных a и b,
# затем меняет их значения местами
# (то есть в переменной a должно быть записано то, что раньше хранилось в b,
# а в переменной b записано то, что раньше хранилось в a).
# Затем выведите значения переменных.

# a = int( input())
# b = int( input())
# d = a
# a =b
# b = d
# print (a,b)


# Задача 5
# Пирожок в столовой стоит a  рублей и b  копеек.
# Определите, сколько рублей и копеек нужно заплатить за n пирожков.

# a = int(input("Сколько рублей стоит пирожок?"))
# b = int(input("Сколько копеек?"))
# c = int(input("Сколько всего пирожков?"))
# print((a + b/100) * c)

# Задача 6
# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?

# n = int(input("расстояние"))
# m = int(input("длина"))
# print(m // n)


# Задача 7
# Имеется N кг металлического сплава.
# Из него изготавливают заготовки массой K кг каждая.
# После этого из каждой заготовки вытачиваются детали массой M кг каждая
# (из каждой заготовки вытачивают максимально возможное количество деталей).
# Если от заготовок после этого что-то остается,
# то этот материал возвращают к началу производственного цикла и сплавляют с тем,
# что осталось при изготовлении заготовок.
# Если того сплава, который получился, достаточно для изготовления хотя бы одной заготовки,
# то из него снова изготавливают заготовки, из них—  детали и т.д.
# Напишите программу, которая вычислит, какое количество деталей может быть получено
#  по этой технологии из имеющихся исходно N кг сплава.

# n = int(input("Сплава:"))
# k = int(input("Масса заготовки:"))
# m = int(input("Масса изделия:"))

# print((n // k) * (k // m))


# пример как решать домашку
x = 567

a = x//100
b = x //10 % 10
c = x % 10

print(a*b*c)