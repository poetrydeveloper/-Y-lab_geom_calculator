import math
from calc.figure.figure import Figure


class Cone(Figure):
    def __init__(self):
        self.__radius = None
        self.__generatrix = None
        self.area = None
        self.volume = None

    def radius(self, args) -> None:
        if float(args[0]) > 0:
            self.__radius = float(args[0])

    def generatrix(self, args) -> None:
        if float(args[1]) > 0:
            self.__generatrix = float(args[1])

    def reassembly(self, args) -> str:
        contain_zero = 0
        for el in args:
            if float(el) <= 0:
                contain_zero += 1
        if not contain_zero:
            self.radius(args)
            self.generatrix(args)
            self.calc_area()
            self.calc_volume()
            return 1
        else:
            return -1

    def calc_volume(self) -> None:
        self.volume = round((1 / 3 * (math.pi * (self.__radius ** 2) * self.__generatrix)), 3)

    def calc_area(self) -> None:
        self.area = round(math.pi * self.__radius * (self.__radius + self.__generatrix), 3)

    def get_area(self) -> float:
        return self.area

    def get_volume(self) -> float:
        return self.volume
