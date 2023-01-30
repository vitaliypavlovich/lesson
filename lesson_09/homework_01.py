'''
Создать класс Point, описывающий точку (атрибуты: x, y).
Создать класс Figure.
Создать три дочерних класса
Circle (атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
'''

class Point:
    x = None
    y = None
    def __init__(self, x, y):
        self.x, self.y = x, y

class Figure:


class Circle(Figure):
    mid = None
    r = None
    def __init__(self, mid, r):
        self.mid, self.r = mid, r

    def peremiter(self):
         return 2 * self.r * 3,14
    def area(self):
        return 3,14 * self.r ** 2

class Triangle(Figure):
    a = None
    b = None
    c = None
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def peremiter(self):
        return self.a + self.b + self.c
    def area(self):
        return 1/2 * (self.a * self.b)

class Sqaure(Figure):


