from calc.figure.figure import Figure


class Square(Figure):
    def __init__(self, side=0):
        self.side = side
        self.revision()

    def revision(self):
        if self.side == 0:
            print("to calculate the length of the side of the square")

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return self.side * 4
