import math
from functools import reduce


class Geometric_figure:

    def __init__(self, name, sides, angles):
        self.name = name
        self.sides = sides
        self.angles = angles

    def get_area(self):
        return self.sides[0] * self.sides[1]

    def get_angles(self):
        return self.angles

    def get_perimeter(self):
        return reduce((lambda x, y: x + y), self.sides)

    def add_area(self, other):
        if isinstance(other, Geometric_figure):
            return self.get_perimeter() + other.get_perimeter()
        else:
            raise RuntimeError("Передан неправильный класс!")


class Triangle(Geometric_figure):
    __name = "Triangle"

    def __init__(self, sides):
        if len(sides) == 3:
            super().__init__(self.__name, sides, 3)
        else:
            raise RuntimeError("Количество сторон отлично от 3")

    def get_area(self):
        p = self.get_perimeter() / 2
        return round(math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])), 1)


class Square(Geometric_figure):
    __name = "Square"

    def __init__(self, sides):
        if len(sides) == 4:
            super().__init__(self.__name, sides, 4)
        else:
            raise RuntimeError("Количество сторон отлично от 4")


class Rectangle(Geometric_figure):
    __name = "Rectangle"

    def __init__(self, sides):
        if len(sides) == 4:
            super().__init__(self.__name, sides, 4)
        else:
            raise RuntimeError("Количество сторон отлично от 4")


class Circle(Geometric_figure):
    __name = "Circle"

    def __init__(self, radius):
        super().__init__(self.__name, radius, 0)

    def get_area(self):
        return round(math.pi * (self.sides[0] ** 2), 1)

    def get_perimeter(self):
        return 2 * math.pi * self.sides[0]
