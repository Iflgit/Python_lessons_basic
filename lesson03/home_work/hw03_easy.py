__author__ = 'Nekhamchin Anatoly'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print("1:")


def my_round(number, ndigits):
    number = number * 10 ** ndigits
    _tail = number % 1
    if _tail >= 0.5:
        number += 1
    return (number - _tail) / 10 ** ndigits


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
try:
    print(my_round(float(input("float: ")), int(input("digits: "))))
except ValueError:
    print("input error")


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print("2:")


def lucky_ticket(ticket_number):
    ticket_number = list(int(x) for x in str(ticket_number))
    return sum(ticket_number[:3]) == sum(ticket_number[-3:]) and len(ticket_number) == 6


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
try:
    print(lucky_ticket(int(input("ticket: "))))
except ValueError:
    print("input error")
