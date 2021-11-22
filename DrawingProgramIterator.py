from typing import List
from Shape import Shape


class DrawingProgramIterator:

    def __init__(self, shapes: List[Shape]) -> None:
        self.__shapes = shapes
        self.__index = 0

    def __next__(self) -> Shape:
        if self.__index == len(self.__shapes):
            raise StopIteration()
        shape = self.__shapes[self.__index]
        self.__index += 1
        return shape

    def __iter__(self):
        return self
