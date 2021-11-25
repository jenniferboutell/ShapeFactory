from typing import Union
from math import sqrt
from Shape import Shape

Number = Union[float, int]


class Triangle(Shape):

    def __init__(self, side1: Number, side2: Number, side3: Number) -> None:
        super().__init__()
        self.__side1: float = float(side1)
        self.__side2: float = float(side2)
        self.__side3: float = float(side3)

    @property
    def side1(self) -> float:
        return self.__side1

    @property
    def side2(self) -> float:
        return self.__side2

    @property
    def side3(self) -> float:
        return self.__side3

    def identical(self, other) -> bool:
        return type(self) == type(other) and \
               {self.side1, self.side2, self.side3} == {other.side1, other.side2, other.side3}

    @property
    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

    @property
    def area(self) -> float:
        sp = self.perimeter / 2
        return sqrt(sp * (sp - self.side1) * (sp - self.side2) * (sp - self.side3))

# END
