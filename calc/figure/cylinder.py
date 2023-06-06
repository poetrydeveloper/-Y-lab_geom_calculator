import math
from calc.figure.figure import Figure


class Cylinder(Figure):
    def __init__(self):

        self.__radius = None
        self.__height = None
        self.area = None
        self.volume = None

    def radius(self, args) -> None:
        if float(args[0]) > 0:
            self.__radius = float(args[0])

    def height(self, args) -> None:
        if float(args[1]) > 0:
            self.__height = float(args[1])

    def reassembly(self, args) -> str:
        contain_zero = 0
        for el in args:
            if float(el) <= 0:
                contain_zero += 1
        if not contain_zero:
            self.radius(args)
            self.height(args)
            self.calc_volume()
            self.calc_area()
            return 1
        else:
            return -1

    def calc_volume(self) -> None:
        self.volume = round(((math.pi * (self.__radius ** 2)) * self.__height), 3)

    def get_volume(self) -> float:
        return self.volume

    def calc_area(self) -> None:
        self.area = round(2 * (math.pi * self.__radius * self.__height) + 2 * math.pi * (self.__radius ** 2), 3)

    def get_area(self) -> float:
        return self.area
