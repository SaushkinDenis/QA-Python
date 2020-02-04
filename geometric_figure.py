import math
from functools import reduce


class Geometric_figure:

    def __init__(self, name, params, angles):
        self.name = name
        self.params = params
        self.angles = angles

    def get_area(self):
        return reduce((lambda x, y: x * y), self.params)

    def get_angles(self):
        return self.angles

    def get_perimeter(self):
        return reduce((lambda x, y: x + y), self.params)

    def add_area(self, other):
        if isinstance(other, Geometric_figure):
            return self.get_perimeter() + other.get_perimeter()
        else:
            raise RuntimeError("Передан неправильный класс!")


class Triangle(Geometric_figure):
    __name = "Triangle"

    def __init__(self, __name, sides):
        if len(sides) == 3:
            super().__init__(__name, sides, 3)
        else:
            raise RuntimeError("Количество сторон отлично от 3")

    def get_area(self):
        p = self.get_perimeter() / 2
        return round(math.sqrt(p * (p - self.params[0]) * (p - self.params[1]) * (p - self.params[2])), 1)


class Rectangle(Geometric_figure):
    __name = "Rectangle"

    def __init__(self, __name, sides):
        if len(sides) == 2:
            super().__init__(__name, sides, 4)
        else:
            raise RuntimeError("Количество сторон отлично от 2")

    def get_perimeter(self):
        return (self.params[0] + self.params[1]) * 2


class Square(Rectangle):
    __name = "Square"

    def __init__(self, __name, side):
        super().__init__(__name, [side, side])


class Circle(Geometric_figure):
    __name = "Circle"

    def __init__(self, radius):
        print(radius)
        super().__init__(self.__name, radius, 0)

    def get_area(self):
        return round(math.pi * (self.params ** 2), 1)

    def get_perimeter(self):
        return 2 * math.pi * self.params
