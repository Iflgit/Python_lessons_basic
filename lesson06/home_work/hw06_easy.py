__author__ = "Nekhamchin Anatoly"
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
print("1:")

import math

class Point:
    def __init__(self, *args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        else:
            raise ValueError("point mast have 2 coord")

    def __str__(self):
        return f"({self.x}, {self.y})"


point1 = Point(0, 0)
#print(point1)


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return math.sqrt((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2)

    def __str__(self):
        return f"{self.p1}-{self.p2}"

point2 = Point(1, 1)
#print(point2)
#line1 = Line(point1, point2)

class Figure:
    def __init__(self, *args):
        if len(args) > 2:
            self.points = []
            for point in args:
                self.points.append(Point(point.x, point.y))
        else:
            raise ValueError("must be 3+ points")

    def length(self, p1, p2):
        return Line(p1, p2).length()

    def perimeter(self):
        _p = 0
        for idx, point in enumerate(self.points[:-1]):
            _p += self.length(point, self.points[idx+1])
        _p += self.length(self.points[-1], self.points[0])
        return _p

    def square(self):
        _s = 0
        for idx, point in enumerate(self.points):
            if idx == 0:
                yminus = self.points[-1].y
            else:
                yminus = self.points[idx-1].y
            if idx == len(self.points)-1:
                yplus = self.points[0].y
            else:
                yplus = self.points[idx+1].y

            _s += point.x*(yplus-yminus)
        return abs(_s/2)

    def height(self, *args):
        _h = Point(args[0].x, args[0].y)
        _oppo = Line(args[1], args[2])
        _height = abs((_oppo.p2.y-_oppo.p1.y)*_h.x-(_oppo.p2.x-_oppo.p1.x)*_h.y+\
                     _oppo.p2.x*_oppo.p1.y-_oppo.p2.y*_oppo.p1.x)/\
                     math.sqrt((_oppo.p2.y-_oppo.p1.y)**2+(_oppo.p2.x-_oppo.p1.x)**2)
        return _height

    def __str__(self):
        _s = self.points[0]
        for point in self.points[1:]:
            _s = f"{_s} {point}"
        return _s


point3 = Point(2, 1)
t1 = Figure(point1, point2, point3)
#print(t1.perimeter())
#print(t1)


class Threeangle(Figure):
    def __init__(self, *args):
        if len(args) == 3:
            super().__init__(*args)
        else:
            raise ValueError("3 points for threeangle")

    # def square(self):
    #     p1 = self.points[0]
    #     p2 = self.points[1]
    #     p3 = self.points[2]
    #     return abs(((p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y)))/2

    # def _length(self, p1, p2):
    #     p1 = self.points[p1-1]
    #     p2 = self.points[p2-1]
    #     return math.sqrt((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2)

    # def height(self, point):
    #     len1 = self._length(1, 2)
    #     len2 = self._length(2, 3)
    #     len3 = self._length(1, 3)
    #     p = (len1 + len2 + len3) / 2
    #     opposit = [1, 2, 3]
    #     opposit.pop(point-1)
    #     print(opposit)
    #     return math.sqrt(p * (p - len1) * (p - len2) * (p - len3)) / self._length(opposit[0], opposit[1]) * 2

    # def perimeter(self):
    #     return(self._length(1, 2) + self._length(2, 3) + self._length(1, 3))


tr1 = Threeangle(point1, point2, point3)
# tr1 = Threeangle((0, 0), (1, 1), (1, 0))


print(f"площадь{tr1}: {tr1.square()}")
h = tr1.height(tr1.points[0], tr1.points[1], tr1.points[2])
print(f"высота из{tr1.points[0]} к {Line(tr1.points[1], tr1.points[2])} = {h}")
#print(f"{tr1.height(1)}")
print(f"периметр:{tr1} {tr1.perimeter()}")
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print("2:")


class Trapeze(Figure):
    def __init__(self, *args):
        if len(args) == 4:
            super().__init__(*args)
        else:
            raise ValueError("need 4 points for trapeze")
        if self.height(self.points[0], self.points[1], self.points[2]) == \
                self.height(self.points[3], self.points[1], self.points[2]) or \
                self.height(self.points[0], self.points[2], self.points[3]) == \
                self.height(self.points[1], self.points[2], self.points[3]):
            print("trapeze")
        else:
            raise ValueError("no trapeze")

    def isequil(self):
        return (self.length(self.points[0], self.points[1]) == self.length(self.points[2], self.points[3]) or\
                self.length(self.points[1], self.points[2]) == self.length(self.points[0], self.points[3]))


trapeze = Trapeze(point1, point2, point3, Point(3, 0))
print(f"четырехугольник: {trapeze}")
print(f"площадь {trapeze} = {trapeze.square()}")
print(f"периметр {trapeze} = {trapeze.perimeter()}")
print(f"длина между вершинами 0 и 3 = {trapeze.length(trapeze.points[0], trapeze.points[3])}")
print(f"две противоположные стороны равны? {trapeze.isequil()}")

