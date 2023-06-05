from calc.figure.figure import Figure


class Trapezoid(Figure):
    def __init__(self, first_side=0, second_side=0, third_side=0, fourth_side=0, height=0):
        self.area = None
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        self.fourth_side = fourth_side
        self.height = height

        self.revision()

    def revision(self):
        if self.second_side == 0 and self.third_side ==0 and self.height == 0:
            print('for calculations in an isosceles trapezoid we need 2 sides and a height')
        self.calc_area()



    def get_area(self):
        return self.area


    def calc_area(self):
        self.area = (self.second_side + self.third_side) * self.height / 2

    def get_perimeter(self):
        return self.first_side + self.second_side + self.third_side + self.fourth_side