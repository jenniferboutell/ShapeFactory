from Shape import Shape

class Rectangle:

    def __init__(self, length, width, area, perimeter):
        self.name = "rectangle"
        self.length = 0
        self.width = 0
        self.area = self.width * self.length
        self.perimeter = 2 * (self.length + self.width)

