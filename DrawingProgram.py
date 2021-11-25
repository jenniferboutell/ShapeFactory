from typing import Optional, List
from Shape import Shape
from DrawingProgramIterator import DrawingProgramIterator


class DrawingProgram:
    """
    A mock "drawing" program, which contains an ordered collection of shapes.
    """

    def __init__(self, shapes: Optional[List[Shape]] = None) -> None:
        """
        Constructor. Initializes shapes collection to the list passed in, if any.

        :param shapes: a list of Shapes or nothing at all.
        """
        if shapes is None:
            shapes = []
        self.__shapes: List[Shape] = shapes

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

    def remove_shape(self, shape: Optional[Shape] = None) -> int:
        """
        Remove from the shapes collection all that are identical to the
        shape passed in. Here, "identical" is in the geometric sense.
        E.g. a Rectangle with length=2 and width=3 is considered identical
        to a Rectangle with length=3 and width=2, i.e. length and width
        are considered interchangeable.

        :param shape: instance of Shape or one of its subclasses.
        :return: The number of shapes removed from the collection.
        """
        if shape is not None and not isinstance(shape, Shape):
            raise TypeError(f"remove_shape expects shape of type None or a Shape subclass, but got {type(shape)}")
        counter = 0
        for s in self.__shapes:
            if shape is None or shape.identical(s):
                self.__shapes.remove(s)
                counter += 1
        return counter

    # @staticmethod  # TODO should not be static, right?
    def print_shape(self, shape: Optional[Shape] = None) -> None:
        """
        Prints all in shapes collection that match the type of the shape passed in.

        :param shape: Instance of Shape or one of its subclasses.
        :return: None
        """
        if shape is not None and not isinstance(shape, Shape):
            raise TypeError(f"print_shape expects shape of either None or Shape subclass, but got {type(shape)}")
        for s in self.__shapes:
            if shape is None or isinstance(s, type(shape)):
                print(s)

    @staticmethod
    def merge_sort(shapes):
        if len(shapes) > 1:
            mid = len(shapes) // 2
            left = shapes[:mid]
            right = shapes[mid:]
            DrawingProgram.merge_sort(left)
            DrawingProgram.merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    shapes[k] = left[i]
                    i = i+1
                else:
                    shapes[k] = right[j]
                    j = j+1
                k = k+1

            while i < len(left):
                shapes[k] = left[i]
                i = i+1
                k = k+1

            while j < len(right):
                shapes[k] = right[j]
                j = j+1
                k = k+1
        return shapes

    def sort_shapes(self) -> None:
        """
        Sorts the collection of shapes, replacing the current collection order.
        Shapes will be sorted first by name, then by area if names are same.
        Uses a sort that runs in O(nlogn) for its worst case, e.g. Merge or Heap.

        :return: None
        """
        self.__shapes = self.merge_sort(self.__shapes)

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
