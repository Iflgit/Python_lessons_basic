# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Table:
    def __init__(self, *args):
        self.sname = args[0]
        self.fname = args[1]
        self.whours = int(args[2])

    def getname(self):
        return f"{self.sname} {self.fname}"


class Worker(Table):
    def __init__(self, dataline):
        _data = dataline.split()
        super().__init__(_data[0], _data[1], _data[4])
        self.salary = int(_data[2])


class WorkHours(Table):
    def __init__(self, dataline):
        _data = dataline.split()
        super().__init__(_data[0], _data[1], _data[2])


data_workers = []
work_hours = []

try:
    with open("data/workers", "r", encoding="UTF-8") as workers_file:
        workers_file.readline()
        for line in workers_file:
            data_workers.append(Worker(line))

    with open("data/hours_of", "r", encoding="UTF-8") as hours_of_file:
        hours_of_file.readline()
        for line in hours_of_file:
            work_hours.append(WorkHours(line))
except IOError:
    print("error reading data files")
    exit(1)
except IndexError:
    print("not enough data in file")
except ValueError:
    print("wrong value")

def salary(s, h1, h2):
    if h1 >= h2:
        return s / h1 * h2
    else:
        return s + s/h1 * 2 * (h2 - h1)


for person in data_workers:
    for hours in work_hours:
        if person.getname() == hours.getname():
            _s = int(salary(person.salary, person.whours, hours.whours))
            print(f"{person.getname()} ({person.whours}*{person.salary}^{hours.whours})-> {_s}RUR)")


