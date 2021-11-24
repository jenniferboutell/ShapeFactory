# import pytest

from ShapeFactory import ShapeFactory
from DrawingProgram import DrawingProgram
# from DrawingProgramIterator import DrawingProgramIterator


def test_dp_init_0():
    exp = []
    dp = DrawingProgram()
    out = [str(s) for s in dp]
    assert out == exp


def test_dp_init_1():
    s1 = ShapeFactory.create_square(2)
    exp = [str(s) for s in [s1]]
    dp = DrawingProgram([s1])
    out = [str(s) for s in dp]
    assert out == exp


def test_dp_init_5():
    s1 = ShapeFactory.create_circle(1)
    s2 = ShapeFactory.create_rectangle(2, 3)
    s3 = ShapeFactory.create_square(3)
    s4 = ShapeFactory.create_triangle(4, 3, 5)
    s5 = ShapeFactory.create_circle(5)
    exp = [str(s) for s in [s1, s2, s3, s4, s5]]
    dp = DrawingProgram([s1, s2, s3, s4, s5])
    out = [str(s) for s in dp]
    assert out == exp


if __name__ == '__main__':
    print("Run pytest, you fool!")

# END
