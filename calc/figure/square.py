from calc.figure.figure import Figure


class Square(Figure):

    def __init__(self):
        self.__side = None
        self.perimeter = None
        self.area = None

    def side(self, args) -> None:
        if float(args[0]) > 0:
            self.__side = float(args[0])

    def reassembly(self, args) -> str:
        contain_zero = 0
        for el in args:
            if float(el) <= 0:
                contain_zero += 1
        if not contain_zero:
            self.side(args)
            self.calc_perimeter()
            self.calc_area()
            return 1
        else:
            return -1

    def calc_perimeter(self) -> None:
        self.perimeter = self.__side * 4

    def get_perimeter(self) -> float:
        return self.perimeter

    def calc_area(self) -> None:
        self.area = round((self.__side ** 2),3)

    def get_area(self) -> float:
        return self.area
