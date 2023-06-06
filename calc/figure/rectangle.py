from math import sqrt
from calc.figure.figure import Figure


class Rectangle(Figure):
    def __init__(self):
        self.__first_side = None
        self.__second_side = None
        self.perimeter = None
        self.area = None
        self.diagonal = None

    def first_side(self, args) -> None:
        if float(args[0]) > 0:
            self.__first_side = float(args[0])

    def second_side(self, args) -> None:
        if float(args[1]) > 0:
            self.__second_side = float(args[1])

    def reassembly(self, args) -> str:
        contain_zero = 0
        for el in args:
            if float(el) <= 0:
                contain_zero += 1
        if not contain_zero:
            self.first_side(args)
            self.second_side(args)
            self.calc_diagonal()
            self.calc_area()
            return 1
        else:
            return -1

    def calc_area(self):
        self.area = self.__first_side * self.__second_side

    def calc_diagonal(self):
        self.diagonal = round(sqrt(self.__first_side * self.__first_side + self.__second_side * self.__second_side), 3)

    def get_area(self) -> float:
        return self.area

    def get_diagonal(self) -> float:
        return self.diagonal
