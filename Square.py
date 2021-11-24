from typing import Union
from Rectangle import Rectangle

Number = Union[float, int]


class Square(Rectangle):

    def __init__(self, length: Number) -> None:
        super().__init__(length, length)

# END
