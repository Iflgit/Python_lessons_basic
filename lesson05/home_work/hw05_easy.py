__author__ = 'Nekhamchin Anatoly'
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print("1:")

import os


cur_dir = os.getcwd()
print(cur_dir)
for idx in range(9):
    md = os.path.join(cur_dir, f'Dir_{idx+1}')
    try:
        os.mkdir(md)
        print(f'+{md} created')
    except FileExistsError:
        print(f'directory {md} exist')

for idx in range(9):
    md = os.path.join(cur_dir, f'Dir_{idx+1}')
    try:
        os.rmdir(md)
        print(f'-{md} deleted')
    except FileNotFoundError:
        print(f'directory {md} not found')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print("2:")

for _dir in list(filter(os.path.isdir, os.listdir(os.getcwd()))):
    print(_dir)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print("3:")

import shutil
import sys

cur_file = sys.argv[0]
try:
    src = os.path.join(os.getcwd(), sys.argv[0])
    dst = os.path.join(os.getcwd(), f'{sys.argv[0]}.copy')
    shutil.copyfile(src, dst)
    print(f'{src}->{dst} ok')
except IOError:
    print(f'no access to {dst}')

