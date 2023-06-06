import math
from calc.figure.figure import Figure


class Pyramid(Figure):
    def __init__(self):
        self.__quantity_of_sides = None
        self.__side = None
        self.__height = None
        self.area_p = None
        self.volume = None
        self.So = None

    def side(self, args) -> None:
        if float(args[0]) > 0:
            self.__side = float(args[0])

    def height(self, args) -> None:
        if float(args[1]) > 0:
            self.__height = float(args[1])

    def quantity_of_sides(self, args) -> None:
        if float(args[2]) > 0:
            self.__quantity_of_sides = float(args[2])

    def reassembly(self, args) -> str:
        contain_zero = 0
        for el in args:
            if float(el) <= 0:
                contain_zero += 1
        if not contain_zero:
            self.side(args)
            self.height(args)
            self.quantity_of_sides(args)
            self.calc_volume()
            self.calc_area()
            return 1
        else:
            return -1

    def calc_area(self):
        r = self.__side / (2 * math.tan(math.pi / self.__quantity_of_sides))
        l: float = math.sqrt(self.__height ** 2 + r ** 2)
        self.area_p = round(self.So + self.__quantity_of_sides * self.__side * l / 2, 1)

    def calc_volume(self):
        self.So = self.__quantity_of_sides * self.__side ** 2 / (4 * math.tan(math.pi / self.__quantity_of_sides))
        self.volume = round(self.So * self.__height / 3, 1)

    def get_volume(self) -> float:
        return self.volume

    def get_area(self) -> float:
        return self.area_p
