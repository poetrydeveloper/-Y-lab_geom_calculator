from typing import Any

from calc.figure.square import Square
from calc.figure.triangle import Triangle
from calc.figure.circle import Circle
from calc.figure.rectangle import Rectangle
from calc.figure.rhombus import Rhombus
from  calc.figure.trapezoid import Trapezoid

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
            case "trapezoid":
                self.active_figure = Trapezoid()
                return ['upper_side', 'down_side', 'height',]
            case "rhombus":
                self.active_figure = Rhombus()
                return ['first_side', 'height',]
            case "rectangle":
                self.active_figure = Rectangle()
                return ['first_side', 'second_side',]
            case "triangle":
                self.active_figure = Triangle()
                return ['first_side', 'second_side', 'third_side',]
            case "square":
                self.active_figure = Square()
                return ['side',]
            case "circle":
                self.active_figure = Circle()
                return ['radius',]

    def insert_param(self, args: list[int]) -> None:
        if self.active_figure:
            method_list = [method for method in dir(self.active_figure) if method.startswith('get')  is True]
            print(method_list)
            try:
                if self.active_figure.reassembly(args) > 0:
                    text = ''
                    for method in method_list:
                        func = f'self.active_figure.{method}()'
                        count = eval(func)
                        sample = "get_"
                        pre_string = f'{method} - {count}\n'
                        pre_string = pre_string.lstrip(sample)
                        text += pre_string

                    return text
            except:
                return (f'Some Error. Check your input.')