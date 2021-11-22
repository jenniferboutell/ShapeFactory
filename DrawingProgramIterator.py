class DrawingProgramIterator:

        def __init__(self, string):
            self.shapes = [shape for shapes in drawing_program]
            self.index = 0

        def __next__(self):
            if self.index == len(self.shapes):
                raise StopIteration()

            shape = self.shapes[self.index]
            self.index += 1
            return shape

        def __iter__(self):
            return self