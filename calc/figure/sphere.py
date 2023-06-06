import math
from calc.figure.figure import Figure


class Sphere(Figure):
    def __init__(self):
        self.__radius = None
        self.volume = None
        self.area = None
        self.diameter = None

    def radius(self, args) -> None:
        if float(args[0]) > 0:
            self.__radius = float(args[0])

    def reassembly(self, args) -> str:
        contain_zero = 0
        for el in args:
            if float(el) <= 0:
                contain_zero += 1
        if not contain_zero:
            self.radius(args)
            self.calc_diameter()
            self.calc_volume()
            self.calc_area()
            return 1
        else:
            return -1

    def calc_diameter(self) -> None:
        self.diameter = self.__radius * 2

    def get_diameter(self) -> float:
        return self.diameter

    def calc_area(self) -> None:
        self.area = round((4 * math.pi * (float(self.__radius) ** 2)), 3)

    def get_area(self) -> float:
        return self.area

    def calc_volume(self):
        self.volume = round(((4 / 3) * (math.pi * float(self.__radius) ** 3)),3)

    def get_volume(self) -> float:
        return self.volume
