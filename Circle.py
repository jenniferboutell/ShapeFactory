from math import pi
from Shape import Shape


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    @property
    def area(self):
        return pi * (float(self.radius) ** 2)

    @property
    def perimeter(self):
        return 2 * pi * self.radius
