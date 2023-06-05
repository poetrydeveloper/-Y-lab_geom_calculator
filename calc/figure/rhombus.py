from calc.figure.figure import Figure


class Rhombus(Figure):
    def __init__(self, first_side=0, height=0,):
        self.first_side = first_side
        self.height = height

        self.revision()

    def revision(self):
        if self.first_side == 0 or self.height == 0:
            print("for calculations we need at least one side and height")

    def get_area(self):
        return self.first_side * self.height

    def perimeter(self):
        return self.first_side * 4


