from typing import Union

from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle
from Circle import Circle


class ShapeFactory:

    @staticmethod
    def create_shape(shape_name: str, *shape_data) -> Union[Circle, Square, Rectangle, Triangle]:
        """
        Creates a shape of the specified type using the necessary data
        for building that shape and returns that shape. e.g.:
        my_shape = ShapeFactory.create_shape("Circle", 2.0),
        where 2.0 is the radius of the circle.
        my_shape = ShapeFactory.create_shape("Rectangle", 2.0, 4.0),
        where 2.0 is length and 4.0 is width.

        :param shape_name: Name of a Shape subclass.
        :param shape_data: One or more values, as appropriate for
            building shape of the specified type.
        :return: newly created shape
        """
        if shape_name == "Rectangle":
            maker = ShapeFactory.create_rectangle
        elif shape_name == "Square":
            maker = ShapeFactory.create_square
        elif shape_name == "Triangle":
            maker = ShapeFactory.create_triangle
        elif shape_name == "Circle":
            maker = ShapeFactory.create_circle
        else:
            raise ValueError(f"make_shape does not support shape_name {shape_name}")
        shape = maker(*shape_data)
        return shape

    @staticmethod
    def create_rectangle(*shape_data) -> Rectangle:
        """
        Builds a new Rectangle.
        As a special case, if length and width are same, instead builds a Square.

        :param shape_data: Length and width of the rectangle.
        :return: newly created Rectangle.
        """
        if len(shape_data) != 2:
            raise ValueError(f"Rectangle requires 2 params, got {len(shape_data)}")
        if shape_data[0] == shape_data[1]:
            return Square(shape_data[0])
        return Rectangle(*shape_data)

    @staticmethod
    def create_square(*shape_data) -> Square:
        """
        Builds a new Square.

        :param shape_data: Side lengths of the square.
        :return: newly created Square.
        """
        return Square(*shape_data)

    @staticmethod
    def create_triangle(*shape_data) -> Triangle:
        """
        Builds a new Triangle.

        :param shape_data: Side lengths of the triangle.
        :return: newly created Triangle.
        """
        return Triangle(*shape_data)

    @staticmethod
    def create_circle(*shape_data) -> Circle:
        """
        Builds a new Circle.

        :param shape_data: Radius of the circle.
        :return: newly created Circle.
        """
        return Circle(*shape_data)

# END
