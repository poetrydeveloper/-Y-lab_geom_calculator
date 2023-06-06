from calc.figure.figure import Figure


class Trapezoid(Figure):
    def __init__(self):
        self.__upper_side = None
        self.__down_side = None
        self.__height = None
        self.perimeter = None
        self.area = None

    def upper_side(self, args) -> None:
        if float(args[0]) > 0:
            self.__upper_side = float(args[0])

    def down_side(self, args) -> None:
        if float(args[1]) > 0:
            self.__down_side = float(args[1])

    def height(self, args) -> None:
        if float(args[1]) > 0:
            self.__height = float(args[1])

    def reassembly(self, args):
        contain_zero = 0
        for el in args:
            if float(el) <= 0:
                contain_zero += 1
        if not contain_zero:
            self.upper_side(args)
            self.down_side(args)
            self.height(args)
            self.calc_perimeter()
            self.calc_area()
            return 1
        else:
            return -1


    def get_area(self):
        return self.area

    def calc_area(self):
        self.area = round(((self.__upper_side + self.__down_side) * self.__height / 2),3)

    def calc_perimeter(self):
        self.perimeter = round((self.__upper_side + self.__upper_side + self.__down_side + self.__down_side),3)
    def get_perimeter(self):
        return self.perimeter