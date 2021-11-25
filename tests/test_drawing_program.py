import pytest

from Circle import Circle
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle

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

def test_dp_sort_shapes_1():
    s1 = ShapeFactory.create_circle(1)
    s2 = ShapeFactory.create_rectangle(2, 3)
    s3 = ShapeFactory.create_square(3)
    s4 = ShapeFactory.create_triangle(4, 3, 5)
    s5 = ShapeFactory.create_circle(5)
    shapes = [s1, s2, s3, s4, s5]
    dp = DrawingProgram(shapes)
    dp.sort_shapes()
    out = [s for s in dp]
    exp = [s1, s5, s2, s3, s4]
    assert out == exp

def test_dp_sort_shapes_empty():
    shapes = []
    dp = DrawingProgram(shapes)
    dp.sort_shapes()
    out = [s for s in dp]
    exp = []
    assert out == exp

def test_dp_sort_shapes_single():
    s1 = Circle(12)
    shapes = [s1]
    dp = DrawingProgram(shapes)
    dp.sort_shapes()
    out = [s for s in dp]
    exp = [s1]
    assert out == exp

def test_dp_sort_shapes_ascending():
    s1 = Circle(1)
    s2 = Circle(2)
    s3 = Rectangle(2, 4)
    s4 = Rectangle (5, 7)
    shapes = [s1, s2, s3, s4]
    dp = DrawingProgram(shapes)
    dp.sort_shapes()
    out = [s for s in dp]
    exp = [s1, s2, s3, s4]
    assert out == exp

def test_dp_sort_shapes_descending():
    s1 = Circle(1)
    s2 = Circle(2)
    s3 = Rectangle(2, 4)
    s4 = Rectangle (5, 7)
    shapes = [s4, s3, s2, s1]
    dp = DrawingProgram(shapes)
    dp.sort_shapes()
    out = [s for s in dp]
    exp = [s1, s2, s3, s4]
    assert out == exp

def test_print_shape(capsys):
    s1 = Square(3)
    s2 = Rectangle(5, 7)
    dp = DrawingProgram([s1,s2])
    dp.print_shape(Rectangle(7,5))
    capt = capsys.readouterr()
    assert capt.out == f"{s2}\n"

def test_add_shape():
    s1 = Circle(4)
    s2 = Triangle(3,4,5)
    s3 = Rectangle(5,7)
    dp = DrawingProgram([s1, s2])
    dp.add_shape(s3)
    exp = [s1, s2, s3]
    out = [s for s in dp]
    assert out == exp

def test_remove_shape():
    s1 = Circle(4)
    s2 = Triangle(3,4,5)
    s3 = Rectangle(5,7)
    dp = DrawingProgram([s1, s2, s3])
    dp.remove_shape(s2)
    exp = [s1, s3]
    out = [s for s in dp]
    assert out == exp

def test__str__():
    s1 = Square(3)
    s2 = Rectangle(5, 7)
    dp = DrawingProgram([s1,s2])
    assert  str(dp) == f"{s1}\n{s2}\n"


def test_dp_get_shape_1():
    """Index not an integer"""
    dp = DrawingProgram()
    with pytest.raises(TypeError):
        dp.get_shape(index="fish")

def test_dp_get_shape_2():
    """empty shapes list"""
    dp = DrawingProgram()
    with pytest.raises(ValueError):
        dp.get_shape(index=1)

def test_dp_get_shape_3():
    """outside range of valid indexes"""
    dp = DrawingProgram([Circle(15)])
    with pytest.raises(ValueError):
        dp.get_shape(index=1)

def test_dp_get_shape_valid():
    """Valid case"""
    s1 = Square(3)
    dp = DrawingProgram([Circle(15), s1, Rectangle(4, 6)])
    out = dp.get_shape(index=1)
    assert out == s1

def test_dp_set_shape_1():
    """Index not an integer"""
    dp = DrawingProgram()
    with pytest.raises(TypeError):
        dp.set_shape(index="fish", shape = Circle(5))

def test_dp_set_shape_2():
    """invalid shape name"""
    dp = DrawingProgram()
    with pytest.raises(TypeError):
        dp.set_shape(index=1, shape = "squirrel")

def test_sp_set_shape_3():
    """empty shapes list"""
    dp = DrawingProgram()
    with pytest.raises(ValueError):
        dp.set_shape(index=1, shape=Circle(15))

def test_sp_set_shape_4():
    """outside range of valid indexes"""
    dp = DrawingProgram([Circle(15)])
    with pytest.raises(ValueError):
        dp.set_shape(index=1, shape=Circle(15))

def test_sp_set_shape_valid():
    """valid case"""
    dp = DrawingProgram([Circle(15)])
    s1 = Square(15)
    exp = [s1]
    dp.set_shape(index=0, shape=s1)
    out = [s for s in dp]
    assert out == exp



if __name__ == '__main__':
    print("Run pytest, you fool!")

# END

