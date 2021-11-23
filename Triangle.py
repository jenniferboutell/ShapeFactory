from Shape import Shape


class Triangle(Shape):

    def __init__(self, side1, side2, side3):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    @property
    def area(self):
        sp = self.perimeter / 2
        return (sp * (sp - self.side1) * (sp - self.side2) * (sp - self.side3)) ** .5



