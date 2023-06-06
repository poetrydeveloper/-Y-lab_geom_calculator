from calc.figure.figure import Figure


class Parallelepiped(Figure):
    def __init__(self):
        self.__first_side = None
        self.__second_side = None
        self.__third_side = None
        self.area = None
        self.volume = None

    def first_side(self, args) -> None:
        if float(args[0]) > 0:
            self.__first_side = float(args[0])

    def second_side(self, args) -> None:
        if float(args[1]) > 0:
            self.__second_side = float(args[1])

    def third_side(self, args) -> None:
        if float(args[2]) > 0:
            self.__third_side = float(args[2])

    def reassembly(self, args) -> str:
        contain_zero = 0
        for el in args:
            if float(el) <= 0:
                contain_zero += 1
        if not contain_zero:
            self.first_side(args)
            self.second_side(args)
            self.third_side(args)
            self.calc_volume()
            self.calc_area()
            return 1
        else:
            return -1

    def calc_volume(self) -> None:
        self.volume = self.__first_side * self.__second_side * self.__third_side

    def get_volume(self) -> any:
        return self.volume

    def calc_area(self) -> None:
        self.area = round(2 * (self.__first_side + self.__second_side + self.__third_side), 3)

    def get_area(self) -> any:
        return self.area
