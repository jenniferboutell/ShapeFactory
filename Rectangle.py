from typing import Union
from Shape import Shape

Number = Union[float, int]


class Rectangle(Shape):

    def __init__(self, length: Number, width: Number) -> None:
        super().__init__()
        self.__length: float = float(length)
        self.__width: float = float(width)

    @property
    def area(self) -> float:
        return self.__width * self.__length

    @property
    def perimeter(self) -> float:
        return 2 * (self.__length + self.__width)

# END
