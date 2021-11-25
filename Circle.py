from typing import Union
from math import pi
from Shape import Shape

Number = Union[float, int]


class Circle(Shape):

    def __init__(self, radius: Number) -> None:
        super().__init__()
        self.__radius = float(radius)

    @property
    def radius(self) -> float:
        return self.__radius

    def identical(self, other) -> bool:
        """
        Determines equality based on type and radius
        :param other:
        :return: equality
        """
        return type(self) == type(other) and self.radius == other.radius

    @property
    def area(self) -> float:
        return pi * (self.radius ** 2)

    @property
    def perimeter(self) -> float:
        return 2 * pi * self.radius

# END
