from math import sqrt

from calc.figure.figure import Figure


class Rectangle(Figure):
    def __init__(self, first_side=0, second_side=0,):
        self.first_side = first_side
        self.second_side = second_side

        self.revision()

    def revision(self):
        if self.first_side == 0 or self.second_side == 0:
            print("for calculations, it is necessary to measure two sides of the rectangle")

    def get_area(self):
        return self.first_side * self.second_side

    def get_diagonal(self):
        return sqrt(self.first_side * self.first_side + self.second_side * self.second_side)


