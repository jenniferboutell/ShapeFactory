from typing import Union
from Shape import Shape

Number = Union[float, int]


class Rectangle(Shape):

    def __init__(self, length: Number, width: Number) -> None:
        super().__init__()
        self.__length: float = float(length)
        self.__width: float = float(width)

    @property
    def length(self) -> float:
        return self.__length

    @property
    def width(self) -> float:
        return self.__width

    def identical(self, other) -> bool:
        return type(self) == type(other) and \
               {self.length, self.width} == {other.length, other.width}

    @property
    def area(self) -> float:
        return self.width * self.length

    @property
    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

# END
