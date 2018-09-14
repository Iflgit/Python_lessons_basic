__author__ = 'Nekhamchin Anatoly'
# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def osn(dr):
    _x, _, _y = dr.partition("/")
    if _y == '':
        return int(_x), 1
    else:
        return int(_x), int(_y)


# eq1 = '5/6 + 4/7'
eq1 = "-2/3 - -2"
#simplify -->
a, sep, b = eq1.partition(" + ")
if sep == '':
    a, sep, b = eq1.partition(" - ")
if sep == " - ":
    sep = sep.strip()
else:
    print(eq1, " wrong equation")
    exit(1)

a = osn(a)
b = osn(b)
res = (0, 0)
if sep == '+':
    res = (a[0] * b[1] + a[1] * b[0], a[1]*b[1])
elif sep == '-':
    res = (a[0] * b[1] - a[1] * b[0], a[1]*b[1])
# <--
# print(res)
sign = ''
if res[0] < 0:
    sign = '-'
    res = (-res[0], res[1])

print("{3}{0} {1}/{2}".format(res[0] // res[1], res[0] % res[1], res[1], sign))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

try:
    with open("data/workers", "r", encoding="UTF-8") as workers_file:
        data_workers = workers_file.read().split("\n")

    with open("data/hours_of", "r", encoding="UTF-8") as hours_of_file:
        data_hours = hours_of_file.read().split("\n")
except IOError:
    print("error reading data files")
    exit(1)

l_hours = []
for line in data_hours:
    l_hours.append(line.split())
# print(l_hours)

l_workers = []
for line in data_workers:
    l_workers.append(line.split())
# print(l_workers)


def salary(s, h1, h2):
    if h1 >= h2:
        return int(s / h1 * h2)
    else:
        return int(s + s/h1 * 2 * (h2 - h1))


for worker in l_workers[1:]:
    for hours in l_hours[1:]:
        if worker[0] + worker[1] == hours[0] + hours[1]:
            print(f"{worker[0]} {worker[1]} ({worker[2]}*{worker[4]}^{hours[2]})->"
                  + str(salary(int(worker[2]), int(worker[4]), int(hours[2]))))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
print("3:")


def cap_letters():
    return list(map(chr, range(ord('А'), ord('Я') + 1)))


with open("data/fruits.txt", "r", encoding="UTF-8") as fruits_file:
    data_fruits = fruits_file.read().split("\n\n")

# print(data_fruits)
# print(cap_letters())
fruit_files = []
for char in cap_letters():
    try:
        _filename = "data/fruits_" + char
        fruit_files.append(open(_filename, 'w', encoding='UTF-8'))
    except IOError:
        print("file recreate error: " + _filename)
        break

for index, char in enumerate(cap_letters()):
    for fruit in data_fruits:
        if fruit.startswith(char):
            try:
                fruit_files[index].write(fruit + '\n')
            except IOError:
                print("file write error")
                break
for fruit_file in fruit_files:
    try:
        fruit_file.close()
    except IOError:
        print("error closing file")

