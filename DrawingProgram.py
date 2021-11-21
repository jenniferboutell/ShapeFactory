import tkinter

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

    def __init__(shapes):
        pass

    def add_shape(shape):
        pass

    def remove_shape(shape):
        pass

    def print_shape(shape):
        pass

    def sort_shapes(self):
        pass

    def __str__(self):
        pass

    def get_shape(index):
        pass

    def set_shape(index, shape):
        pass
