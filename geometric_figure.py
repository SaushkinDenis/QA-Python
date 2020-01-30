class Geometric_Figure:

    def __init__(self, name, area, angles, perimeter):
        self.name = name
        self.area = area
        self.angles = angles
        self.perimeter = perimeter

    def get_area(self):
        return self.area

    def get_angles(self):
        return self.angles

    def get_perimeter(self):
        return self.perimeter

    def add_area(self, other):
        if isinstance(other, Geometric_Figure):
            return self.perimeter + other.get_perimeter()
        else:
            raise ("Передан неправильный класс!")


class Triangle(Geometric_Figure):
    def __init__(self, area, perimeter):
        super().__init__("Triangle", area, 3, perimeter)


class Rectangle(Geometric_Figure):
    def __init__(self, area, perimeter):
        super().__init__("Rectangle", area, 4, perimeter)


class Square(Geometric_Figure):
    def __init__(self, area, perimeter):
        super().__init__("Square", area, 4, perimeter)


class Circle(Geometric_Figure):
    def __init__(self, area, perimeter):
        super().__init__("Circle", area, 0, perimeter)


a = Triangle(1, 1)
b = Triangle(1, 1)
print(a.add_area(b))
