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
        self.__shape_factory = ShapeFactory()

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
        sf = self.__shape_factory

        print("Adding a square, a circle, another square...")
        shape: Shape = sf.create_square(2)
        dp.add_shape(shape)
        shape = sf.create_circle(2)
        dp.add_shape(shape)
        shape = sf.create_square(3.1)
        dp.add_shape(shape)

        print("Printing all shapes...")
        dp.print_shape()
        print("Printing all squares...")
        shape = sf.create_square(1)
        dp.print_shape(shape)
        print("Printing all circles...")
        shape = sf.create_circle(1)
        dp.print_shape(shape)

        print("Sorting shapes...")
        dp.sort_shapes()
        print("Printing all shapes...")
        dp.print_shape()

        print("Removing all squares...")
        shape = sf.create_square(5)
        dp.remove_shape(shape)
        print("Adding a square, a circle...")
        dp.add_shape(shape)
        shape = sf.create_circle(3)
        dp.add_shape(shape)
        print("Printing all shapes...")
        dp.print_shape()

        print("Replacing second shape with a triangle...")
        shape = sf.create_triangle(3, 4, 5)
        dp.set_shape(1, shape)
        print("Adding a rectangle...")
        shape = sf.create_rectangle(2, 3)
        dp.add_shape(shape)
        print("Printing all shapes...")
        dp.print_shape()

        print("Sorting shapes (again)...")
        dp.sort_shapes()
        print("Printing all shapes...")
        dp.print_shape()


if __name__ == "__main__":
    dpm = DrawingProgramMain()
    dpm.run()

# END
