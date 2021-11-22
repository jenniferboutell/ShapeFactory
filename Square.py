from Shape import Shape

class Square:

    def __init__(self, name, length, area, perimeter):
        self.name = "square"
        self.length = 0
        self.area = self.length ** 2
        self.perimeter = self.length * 4
