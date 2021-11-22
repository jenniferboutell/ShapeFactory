from Shape import Shape


class Circle:

    def __init__(self, name, radius, area, perimeter):
        self.name = "circle"
        self.radius = 0
        self.area = 3.14159265 * (float(self.radius) ** 2)
        self.perimeter = 2 * 3.14159265 * radius
