from typing import Any

from calc.figure.triangle import Triangle


class Calculator:
    def __init__(self, figure_name=None):
        self.answers = None
        self.active_figure = None
        self.__figure_name = figure_name

    @property
    def figure_name(self):
        return self.__figure_name

    @figure_name.setter
    def figure_name(self, figure_name):
        self.__figure_name = figure_name

    def get_figure_info(self):
        match self.figure_name:
            case "Триугольник":
                self.active_figure = Triangle()
                self.answers =["Площадь", "Периметр"]
                return ["Первая сторона", "Вторая сторона", "Третья сторона"]

    def insert_param(self, args: list[int]) -> None:
        if self.active_figure:
            try:
                if self.active_figure.reassembly(args) > 0:
                    print('все ок')
                    return (f' {self.answers[0]} - {self.active_figure.get_area()} \n'
                          f' {self.answers[1]} - {self.active_figure.get_perimeter()} ')
            except:
                return (f'Ошибка')