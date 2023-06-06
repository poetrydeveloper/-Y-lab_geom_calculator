from typing import Any

from calc.figure.square import Square
from calc.figure.triangle import Triangle
from calc.figure.circle import Circle


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
            case "triangle":
                self.active_figure = Triangle()
                return ["first_side", "second_side", "third_side"]

            case "square":
                self.active_figure = Square()
                return ["side",]

            case "circle":
                self.active_figure = Square()
                return ["radius", ]

    def insert_param(self, args: list[int]) -> None:
        if self.active_figure:
            # method_list = [method for method in dir(self.active_figure) if method.startswith('get')  is True]
            # print(method_list)
            #method_list = [method for method in dir(self.active_figure) if not method.startswith('get')  is True]
            print ([arg for arg in dir(self.active_figure) if callable(getattr(self.active_figure, arg))])
            #print(method_list2)
            try:
                if self.active_figure.reassembly(args) > 0:
                    text = ''
                    for method in method_list:
                        func = f'self.active_figure.{method}()'
                        count = eval(func)
                        text += f'{method} - {count}\n'
                    return text
            except:
                return (f'Some Error. Check your input.')