from Shape import Shape


class Triangle:

    def __init__(self, name, side1, side2, side3, area, perimeter, sp):
        self.name = "triangle"
        self.side1 = 0
        self.side2 = 0
        self.side3 = 0
        self.perimeter = self.side1 + self.side2 + self.side3
        self.sp = self.perimeter / 2
        self.area = (self.sp * (self.sp - self.side1) * (self.sp - self.side2) * (self.sp - self.side3)) ** .5



