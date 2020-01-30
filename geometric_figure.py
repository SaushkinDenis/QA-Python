import math


class Geometric_figure:

    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def get_area(self):
        return self.sides[0] * self.sides[1]

    def get_angles(self):
        return 4

    def get_perimeter(self):
        area = 0
        for i in self.sides:
            area += i
        return area

    def add_area(self, other):
        if isinstance(other, Geometric_figure):
            return self.get_perimeter() + other.get_perimeter()
        else:
            raise RuntimeError("Передан неправильный класс!")


class Triangle(Geometric_figure):
    def __init__(self, sides):
        if len(sides) == 3:
            super().__init__("Triangle", sides)
        else:
            raise RuntimeError("Количество сторон отлично от 3")

    def get_area(self):
        p = self.get_perimeter() / 2
        return round(math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])), 1)

    def get_angles(self):
        return 3


class Square(Geometric_figure):
    def __init__(self, sides):
        if len(sides) == 4:
            super().__init__("Square", sides)
        else:
            raise RuntimeError("Количество сторон отлично от 4")


class Rectangle(Geometric_figure):
    def __init__(self, sides):
        if len(sides) == 4:
            super().__init__("Rectangle", sides)
        else:
            raise RuntimeError("Количество сторон отлично от 4")


class Circle(Geometric_figure):
    def __init__(self, radius):
        super().__init__("Circle", radius)



    def get_area(self):
        return round(math.pi * (self.sides[0] ** 2), 1)

    def get_perimeter(self):
        return 2 * math.pi * self.sides[0]

    def get_angles(self):
        return 0

    def get_perimeter(self):
        return 2 * math.pi * self.sides[0]


a = Circle([1])

print(a.get_perimeter())