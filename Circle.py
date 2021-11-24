from typing import Union
from math import pi
from Shape import Shape

Number = Union[float, int]


class Circle(Shape):

    def __init__(self, radius: Number) -> None:
        super().__init__()
        self.__radius = float(radius)

    @property
    def area(self) -> float:
        return pi * (self.__radius ** 2)

    @property
    def perimeter(self) -> float:
        return 2 * pi * self.__radius

# END
