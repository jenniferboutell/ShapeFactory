# import pytest
from typing import Union
from math import pi

from Shape import Shape
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle
from Circle import Circle
from ShapeFactory import ShapeFactory

Number = Union[float, int]


class MockShape(Shape):

    def __init__(self, arg1: Number, arg2: Number) -> None:
        super().__init__()
        self.__arg1 = arg1
        self.__arg2 = arg2

    @property
    def area(self) -> float:
        return 0.0

    @property
    def perimeter(self) -> float:
        return 0.0


def test_mock_shape(capsys):
    s = MockShape(1, 2)
    assert isinstance(s, MockShape)
    assert s.area == 0.0
    assert s.perimeter == 0.0
    assert str(s) == f"MockShape, area: {s.area}, perimeter: {s.perimeter}"
    s.draw()
    capt = capsys.readouterr()
    assert capt.out == f"{s}\n"


def test_rectangle(capsys):
    s = Rectangle(3, 2)
    assert isinstance(s, Rectangle)
    assert s.area == 6.0
    assert s.perimeter == 10.0
    assert str(s) == f"Rectangle, area: {s.area}, perimeter: {s.perimeter}"
    s.draw()
    capt = capsys.readouterr()
    assert capt.out == f"{s}\n"


def test_square(capsys):
    s = Square(5)
    assert isinstance(s, Square)
    assert s.area == 25.0
    assert s.perimeter == 20.0
    assert str(s) == f"Square, area: {s.area}, perimeter: {s.perimeter}"
    s.draw()
    capt = capsys.readouterr()
    assert capt.out == f"{s}\n"


def test_triangle(capsys):
    s = Triangle(3, 4, 5)
    assert isinstance(s, Triangle)
    assert s.area == 6.0
    assert s.perimeter == 12.0
    assert str(s) == f"Triangle, area: {s.area}, perimeter: {s.perimeter}"
    s.draw()
    capt = capsys.readouterr()
    assert capt.out == f"{s}\n"


def test_circle(capsys):
    s = Circle(3)
    assert isinstance(s, Circle)
    assert s.area == 9. * pi
    assert s.perimeter == 6. * pi
    assert str(s) == f"Circle, area: {s.area}, perimeter: {s.perimeter}"
    s.draw()
    capt = capsys.readouterr()
    assert capt.out == f"{s}\n"


def test_shape_factory():
    """
    Could have implemented __eq__ in each of the Shape subclasses,
    but easier to simply lean on __str__.
    """
    a = Rectangle(3, 2)
    b = ShapeFactory.create_rectangle(3, 2)
    assert str(a) == str(b)
    b = ShapeFactory.create_shape("Rectangle", 3, 2)
    assert str(a) == str(b)

    a = Square(5)
    b = ShapeFactory.create_square(5)
    assert str(a) == str(b)
    b = ShapeFactory.create_shape("Square", 5)
    assert str(a) == str(b)

    a = Triangle(3, 4, 5)
    b = ShapeFactory.create_triangle(3, 4, 5)
    assert str(a) == str(b)
    b = ShapeFactory.create_shape("Triangle", 3, 4, 5)
    assert str(a) == str(b)

    a = Circle(3)
    b = ShapeFactory.create_circle(3)
    assert str(a) == str(b)
    b = ShapeFactory.create_shape("Circle", 3)
    assert str(a) == str(b)


if __name__ == '__main__':
    print("Run pytest, you fool!")
