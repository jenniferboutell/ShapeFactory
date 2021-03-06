# from typing import List

from DrawingProgram import DrawingProgram
from Shape import Shape
from ShapeFactory import ShapeFactory


class DrawingProgramMain:

    def __init__(self) -> None:
        """
        Constructor. Creates a DrawingProgram and a ShapeFactory.
        """
        self.__drawing_program = DrawingProgram([])

    def run(self):
        """
        Create a class called DrawingProgramMain that creates a DrawingProgram,
        With the DrawingProgram, do the following:
        - Adds shapes to it.
        - Sorts the shapes
        - Adds some more shapes
        - Replaces some shapes
        - Sort the shapes again.
        With each thing done be sure and include print statements to show what was done.
        """
        dp = self.__drawing_program

        print("Adding a square, a circle, another square...")
        shape: Shape = ShapeFactory.create_square(2)
        dp.add_shape(shape)
        shape = ShapeFactory.create_circle(2)
        dp.add_shape(shape)
        shape = ShapeFactory.create_square(3.1)
        dp.add_shape(shape)

        print("Printing all shapes...")
        dp.print_shape()
        print()
        print("Printing all squares...")
        shape = ShapeFactory.create_square(1)
        dp.print_shape(shape)
        print()
        print("Printing all circles...")
        shape = ShapeFactory.create_circle(1)
        dp.print_shape(shape)
        print()

        print("Sorting shapes...")
        dp.sort_shapes()
        print("Printing all shapes...")
        dp.print_shape()
        print()

        print("Removing square with side length 3.1...")
        shape = ShapeFactory.create_square(3.1)
        dp.remove_shape(shape)
        print("Adding a square, a circle...")
        shape = ShapeFactory.create_square(7)
        dp.add_shape(shape)
        shape = ShapeFactory.create_circle(3)
        dp.add_shape(shape)
        print("Printing all shapes...")
        dp.print_shape()
        print()

        print("Replacing second shape with a triangle...")
        shape = ShapeFactory.create_triangle(3, 4, 5)
        dp.set_shape(1, shape)
        print("Adding a rectangle...")
        shape = ShapeFactory.create_rectangle(2, 3)
        dp.add_shape(shape)
        print("Printing all shapes...")
        dp.print_shape()
        print()

        print("Sorting shapes (again)...")
        dp.sort_shapes()
        print("Printing all shapes...")
        dp.print_shape()
        print()


if __name__ == "__main__":
    dpm = DrawingProgramMain()
    dpm.run()

# END
