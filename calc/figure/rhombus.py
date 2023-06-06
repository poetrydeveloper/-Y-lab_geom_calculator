from calc.figure.figure import Figure


class Rhombus(Figure):
    def __init__(self):
        self.__first_side = None
        self.__height = None
        self.perimeter = None
        self.area = None

    def first_side(self, args) -> None:
        if float(args[0]) > 0:
            self.__first_side = float(args[0])

    def height(self, args) -> None:
        if float(args[1]) > 0:
            self.__height = float(args[1])

    def reassembly(self, args):
        contain_zero = 0
        for el in args:
            if float(el) <= 0:
                contain_zero += 1
        if not contain_zero:
            self.first_side(args)
            self.height(args)
            self.calc_perimeter()
            self.calc_area()
            return 1
        else:
            return -1

    def calc_perimeter(self) -> None:
        self.perimeter = round((self.__first_side * 4),3)

    def get_perimeter(self) -> any:
        return self.perimeter

    def calc_area(self) -> None:
        self.area = round((self.__first_side * self.__height),3)

    def get_area(self) -> any:
        return self.area
