import math

from calc.figure.figure import Figure


class Circle(Figure):

    def __init__(self):
        self.__radius = None
        self.circle = None
        self.area = None
        self.diameter = None

    def radius(self, args) -> None:
        if float(args[0]) > 0:
            self.__radius = float(args[0])

    def reassembly(self, args):
        contain_zero = 0
        for str in args:
            if float(str) <= 0:
                contain_zero += 1
        if not contain_zero:
            self.radius(args)
            self.calc_diameter()
            self.calc_circle()
            self.calc_area()
            return 1
        else:
            return -1

    def calc_diameter(self) -> None:
        self.diameter =  self.__radius * 2

    def get_diameter(self):
        return self.diameter

    def calc_area(self) -> None:
        self.area = math.pi * (self.__radius**2)

    def get_area(self) -> None:
        return self.area

    def calc_circle(self):
        self.circle =  2 * math.pi * self.__radius

    def get_circle(self) -> None:
        return self.circle
