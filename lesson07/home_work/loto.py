__author__ = "Nekhamchin Anatoly"
#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
#card(numbers), barrel(numbers 1-90)
Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Barrels:
    def __init__(self, count):
        self._barrels = list()
        for idx in range(count):
            self._barrels.append(idx+1)

    def __len__(self):
        return len(self._barrels)

    def __str__(self):
        return str(self._barrels)

    def get_barrel(self):
        if not len(self._barrels):
            raise IndexError("no more barrels")
        barrel = random.choice(self._barrels)
        self._barrels.remove(barrel)
        print(f"Новый бочонок: {barrel} (осталось {len(self._barrels)})")
        return barrel


class Card:
    def __init__(self):
        _numbers = random.sample(range(91)[1:], 15)
        self._s1 = sorted(_numbers[:5])
        for i in range ( 4 ):
            self._s1.insert(random.randint(0, len(self._s1)), '')
        self._s2 = sorted(_numbers[5:10])
        for i in range ( 4 ):
            self._s2.insert(random.randint(0, len(self._s2)), '')
        self._s3 = sorted(_numbers[10:15])
        for i in range ( 4 ):
            self._s3.insert(random.randint(0, len(self._s3)), '')
        self.pole = list()
        self.pole.extend(self._s1)
        self.pole.extend(self._s2)
        self.pole.extend(self._s3)
        print(self.pole)

    def is_exist(self, num):
        return self.pole.count(num) > 0

    def mark(self, num):
        if self.pole.count(num):
            self.pole[self.pole.index(num)] = ''
        return self.pole.count('')

    def show(self):
        # print('*'*9*5)
        _tmp = '{:^5}'*9
        print(_tmp.format(*self.pole[:9]))
        print(_tmp.format(*self.pole[9:18]))
        print(_tmp.format(*self.pole[18:27]))
        print('*'*9*5)
        return ''


barrels = Barrels(90)
card1 = Card()
card2 = Card()
gameover = False
userinput = ''
while not gameover:
    barrel = barrels.get_barrel()
    print("{:*^45}".format(" computer card "))
    card1.show()
    print("{:*^45}".format(" user card "))
    card2.show()
    if card1.is_exist(barrel):
        if card1.mark(barrel) == 27:
            print("computer win")
            gameover = True
    if userinput == 'auto':
        if card2.is_exist(barrel):
            if card2.mark(barrel) == 27:
                print("user win")
                gameover = True
    else:
        userinput = input("Зачеркнуть цифру? (y/n/auto)")
        if userinput == 'y':
            if card2.is_exist(barrel):
                if card2.mark(barrel) == 27:
                    print("user win")
                    gameover = True
            else:
                print("user loose")
                gameover = True
        if userinput == 'n':
            if card2.is_exist(barrel):
                print("user loose")
                gameover = True
        if userinput == 'auto':
            if card2.is_exist(barrel):
                if card2.mark(barrel) == 27:
                    print("user win")
                    gameover = True


# for idx in range(90):
#     barrels.get_barrel()
#     print(barrels)
