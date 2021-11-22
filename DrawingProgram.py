import tkinter
from Shape import Shape

"""Attributes(instance fields/data)
a list/collection of Shapes
any other data you feel is necessary for the class
Behaviors(methods)
a constructor/init that can be passed a list of Shapes or nothing at all
add_shape(Shape): a method that adds a Shape
remove_shape(Shape): a method that removes ALL shapes that match the one passed as a parameter -- 
it should return in integer value to signify how many of that shape was removed
print_shape(Shape): prints all shapes that match the type of the shape passed in
sort_shapes(): sorts the list/collection of shapes -- you must use a sort that runs in O(nlogn) for its worst case
shapes will be sorted first by name, then by area if names are same
__str__: returns a string representation of each of the shapes -- each shape will be separated from others 
by a newline (\n)
get_shape(index): returns the shape at the specified index
set_shape(index, Shape): replaces the shape at the specified index
any other behaviors you feel are necessary for the class"""

class DrawingProgram:

    def __init__(self, shapes):
        Shape.__init__(self)
        self.shapes = []

    def add_shape(self, Shape):
        self.shapes.append(Shape)

    def remove_shape(self, Shape):
        counter = 0
        for shape in self.shapes:
            if shape == self.Shape:
                self.shapes.remove(shape)
                counter += 1
        return counter

    def print_shape(self, shape):
        Shape.draw(self.shape)

    def sort_shapes(self):
        pass

    def __str__(self):
        return self.name + ", area: " + str(self.area) + ", perimeter: " + str(self.perimeter)

    def get_shape(self, index):
        pass

    def set_shape(self, index, shape):
        pass

