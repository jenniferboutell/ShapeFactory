from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    """
    Attributes
    - name of shape
    Behaviors
    - property to get the name of the shape
      from book see chapter "When to Use Object Oriented Programming"
      and section titled "Adding behaviors to class data with properties"
    - area(): abstract method that will return the area of the given shape
    - perimeter(): abstract method that will return the perimeter of the given shape
    - draw(): prints the name of the shape followed by the area and perimeter of the shape
      formatted as follows: "name_of_shape, area: value_of_area, perimeter: value_of_perimeter"
      e.g."Circle, area: 3.141592653589793, perimeter: 6.283185307179586"
      Note that building a __str__ method would allow draw() to call this method
      and print out the results :-)
    - any other methods you deem necessary

    NOTE: since you are going to have to sort shapes in DrawingProgram, you will
    likely want to provide necessary features to make it easy to sort your shapes
    """

    def __init__(self) -> None:
        self.__name: str = str(self.__class__.__name__)

    def __str__(self) -> str:
        return f"{self.name}, area: {self.area}, perimeter: {self.perimeter}"

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def identical(self, other) -> bool:
        """
        Test for equivalence between two shapes, in a geometric sense, e.g.:
        type(self) == type(other) and
        {self.attr1, self.attr2, ...} == {other.attr1, other.attr2, ...}
        For the types of shapes supported here, attributes are interchangeable,
        i.e. length/width in Rectangle and three sides in Triangle.
        For example, a Rectangles with length=2 and width=3 is considered
        identical to a rectangle with length=3 and width=2.

        :param other:
        :return:
        """
        pass

    def __eq__(self, other) -> bool:
        """
        Equality operator, adhering to match criteria in DrawingProgram::sort_shapes(),
        for which the match criteria is only that both of the following match:
        * object type (as reflected in its .name property)
        * shape area (computed from underlying attributes)

        In other words, it does NOT adhere to more traditional sense of equivalence,
        wherein all the underlying attributes must be equal (e.g. .length and .width
        in a Rectangle). So for example, Rectangles with dimensions 3x8 and 4x6 are
        considered equal here, because they both have area 24.

        :param other: another object belonging to a Shape subclass.
        :return: True for "equals", False otherwise.
        """
        if not issubclass(type(other), Shape):
            raise TypeError(f"__eq__ expects rhs type is Shape subclass, not {type(other)}")
        return self.name == other.name and self.area == other.area

    def __lt__(self, other) -> bool:
        """
        Less-than operator, adhering to match criteria in DrawingProgram::sort_shapes(),
        for which the criteria is only that both of the following match:
        * different shape types, based on lexical comparison of respective names.
        * same shape type, based numerical comparison of respective area values.

        :param other: another object belonging to a Shape subclass.
        :return: True for "less than", False otherwise.
        """
        if not issubclass(type(other), Shape):
            raise TypeError(f"__lt__ expects rhs type is Shape subclass, not {type(other)}")
        if self.name != other.name:
            return self.name < other.name
        return self.area < other.area

    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

    def draw(self) -> None:
        print(self)

# END
