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
