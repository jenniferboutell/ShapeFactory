from Shape import Shape


class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

