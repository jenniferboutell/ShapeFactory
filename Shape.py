

"""Attributes
name of shape
Behaviors
property to get the name of the shape
from book see chapter "When to Use Object Oriented Programming" 
and section titled "Adding behaviors to class data with properties"
area(): abstract method that will return the area of the given shape
perimeter(): abstract method that will return the perimeter of the given shape
draw(): prints the name of the shape followed by the area and perimeter of the shape 
formatted as follows: "name_of_shape, area: value_of_area, perimeter: value_of_perimeter"(
e.g."Circle, area: 3.141592653589793, perimeter: 6.283185307179586")
Note that building a __str__ method would allow draw() to call this method and print out the results :-)
any other methods you deem necessary
NOTE: since you are going to have to sort shapes in DrawingProgram you will likely want to provide necessary 
features to make it easy to sort your shapes"""


class Shape:

    name = property(DrawingProgram.get_shape)

    def area(self):
        pass

    def perimeter(self):
        pass

    def draw(self):
        print(self.name + ", area: " + str(self.area) + ", perimeter: " + str(self.perimeter))

    def __str__(self):
        pass
