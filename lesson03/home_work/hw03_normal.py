__author__ = 'Nekhamchin Anatoly'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("1:")


def fibonacci(n, m):
    _f = [1, 1]
    _i = 0
    if n < 1:
        raise ValueError
    while _i < (m - 2):
        _f.append(_f[-1] + _f[-2])
        _i += 1
    return _f[n-1:m]


print(fibonacci(5, 8))
try:
    print(fibonacci(int(input("n: ")), int(input("m: "))))
except ValueError:
    print("input error")

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print("2:")


def sort_to_max(origin_list):
    _sorted = []
    _i = 0
    _len = len(origin_list)
    while _i < _len:
        _sorted.append(origin_list.pop(origin_list.index(min(origin_list))))
        _i += 1

    return _sorted


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print(sort_to_max([]))
print(sort_to_max(['a', "c", "b"]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print("3:")


def my_filter(func, *args):
    _out = []
    for item in args:
        if func(item):
            _out.append(item)
    return _out


print(list(my_filter(lambda x: x >= 2, 2, 10, -10, 8, 2, 0, 14)))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print("4:")

import math
p4 = (0, 0)
p3 = (3, 0)
p2 = (0, 2)
p1 = (3, 2)


def line_length(a1, a2):
    return math.sqrt((a1[0]-a2[0]) ** 2 + (a1[1]-a2[1]) ** 2)


print(line_length(p1, p2) == line_length(p3, p4) and
        line_length(p2, p3) == line_length(p4, p1)) or \
        (line_length(p1, p3) == line_length(p2, p4) and
        line_length(p1, p4) == line_length(p3, p2))

'''Задача 2 (альтернативная):
Напишите пожалуйста программу, которая открыват файл на запись, 
записывает туда N случайных чисел от -100 до 100
после этого, закрывает файл.
открывает файл снова для чтения, читает оттуда числа, и все числа, 
которые больше 0 записывает в новый файл.'''
print("2*")

import random

try:
    N = int(input("N: "))
except ValueError:
    print("error value")
    exit(1)

i = 0
with open('rand.txt', 'wt', encoding='UTF-8') as random_file:
    while i < N:
        random_file.write(str(random.randint(-100, 100)) + '.')
        i += 1
with open('rand.txt', 'rt', encoding= 'UTF-8') as random_file:
    _values = random_file.read().split('.')
    print(_values)
    with open('abs.txt', 'wt', encoding='UTF-8') as abs_file:
        for _item in _values[:-1]:
            if int(_item) > 0:
                abs_file.write(_item + '\n')

'''Задача 4 (альтернативная):
Напишите функцию, которая считает сумму квадратов от своих аргументов. 
Кол-во аргументов функции может быть любым.

Можно присылать решение для любой из задач: основного или альтернативного'''
print("4*:")


def quad(*args):
    _res = 0
    for _arg in args:
        _res += float(_arg)**2
    return _res

print(quad(True, 2, "3.0"))