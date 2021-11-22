from typing import Optional, List
from Shape import Shape
from DrawingProgramIterator import DrawingProgramIterator


class DrawingProgram:
    """
    A mock "drawing" program, which contains an ordered collection of shapes.
    """

    def __init__(self, shapes: Optional[List[Shape]]) -> None:
        """
        Constructor. Initializes shapes collection to the list passed in, if any.

        :param shapes: a list of Shapes or nothing at all.
        """
        if shapes is None:
            shapes = []
        self.__shapes = shapes

    def __iter__(self):
        """
        Returns an iterator for shapes collection.

        :return: Iterator for shapes collection.
        """
        return DrawingProgramIterator(self.__shapes)

    def __str__(self):
        """
        Returns a string representation of each of the shapes.
        Each shape will be separated from others by a newline (\n).

        :return: String representation.
        """
        return ''.join([f"{s}\n" for s in self.__shapes])

    def add_shape(self, shape: Shape) -> None:
        """
        Add a Shape to the shapes collection.

        :param shape: Instance of a Shape subclass.
        :return: None.
        """
        if not isinstance(shape, Shape):
            raise TypeError(f"add_shape expects shape of type Shape or subclass, but got {type(shape)}")
        self.__shapes.append(shape)

    def remove_shape(self, shape: Shape) -> int:
        """
        Remove from the shapes collection all that match type the shape passed in.

        :param shape: instance of Shape or one of its subclasses.
        :return: The number of shapes removed from the collection.
        """
        if not isinstance(shape, Shape):
            raise TypeError(f"remove_shape expects shape of type Shape or subclass, but got {type(shape)}")
        counter = 0
        for s in self.__shapes:
            if shape == s:
                self.__shapes.remove(s)
                counter += 1
        return counter

    @staticmethod
    def print_shape(shape: Shape) -> None:
        """
        Prints all in shapes collection that match the type of the shape passed in.

        :param shape: Instance of Shape or one of its subclasses.
        :return: None
        """
        if not isinstance(shape, Shape):
            raise TypeError(f"print_shape expects shape of type Shape or subclass, but got {type(shape)}")
        print(shape)

    def sort_shapes(self) -> None:
        """
        Sorts the collection of shapes, replacing the current collection order.
        Shapes will be sorted first by name, then by area if names are same.
        Uses a sort that runs in O(nlogn) for its worst case, e.g. Merge or Heap.

        :return: None
        """
        # TODO in-place Merge sort
        pass

    def get_shape(self, index: int) -> Optional[Shape]:
        """
        Returns the shape at the specified index in shapes collection.

        :param index: A valid index in the shapes collection.
        :return: Specified element in shapes collection.
        """
        if not isinstance(index, int):
            raise TypeError(f"get_shape expects index of type int, but got {type(index)}")
        if len(self.__shapes) == 0:
            raise ValueError(f"get_shape cannot succeed; no shapes in collection")
        if not 0 <= index < len(self.__shapes):
            raise ValueError(f"get_shape expects index in valid range")
        return self.__shapes[index]

    def set_shape(self, index: int, shape: Shape) -> None:
        """
        Replaces the shape at the specified index in collection.

        :param index: A valid index in the shapes collection.
        :param shape: Instance of Shape subclass to replace current element.
        :return: None
        """
        if not isinstance(index, int):
            raise TypeError(f"set_shape needs index of type int, but got {type(index)}")
        if not isinstance(shape, Shape):
            raise TypeError(f"set_shape needs shape of type Shape or subclass, but got {type(shape)}")
        if len(self.__shapes) == 0:
            raise ValueError(f"set_shape cannot succeed; no shapes in collection")
        if not 0 <= index < len(self.__shapes):
            raise ValueError(f"set_shape needs index in valid range")
        self.__shapes[index] = shape
