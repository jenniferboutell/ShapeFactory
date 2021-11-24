from typing import Union
from Shape import Shape

Number = Union[float, int]


class Triangle(Shape):

    def __init__(self, side1: Number, side2: Number, side3: Number) -> None:
        super().__init__()
        self.__side1 = float(side1)
        self.__side2 = float(side2)
        self.__side3 = float(side3)

    @property
    def perimeter(self) -> float:
        return self.__side1 + self.__side2 + self.__side3

    @property
    def area(self) -> float:
        sp = self.perimeter / 2
        return (sp * (sp - self.__side1) * (sp - self.__side2) * (sp - self.__side3)) ** .5

# END
