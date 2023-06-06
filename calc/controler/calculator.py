from calc.figure.square import Square
from calc.figure.triangle import Triangle
from calc.figure.circle import Circle
from calc.figure.rectangle import Rectangle
from calc.figure.rhombus import Rhombus
from calc.figure.trapezoid import Trapezoid
from calc.figure.sphere import Sphere
from calc.figure.pyramid import Pyramid
from  calc.figure.parallelepiped import Parallelepiped
from calc.figure.cylinder import Cylinder
from calc.figure.cube import Cube
from calc.figure.cone import Cone

class Calculator:
    def __init__(self, figure_name=None):
        self.answers = None
        self.active_figure = None
        self.__figure_name = figure_name

    @property
    def figure_name(self) -> str:
        return self.__figure_name

    @figure_name.setter
    def figure_name(self, figure_name) -> None:
        self.__figure_name = figure_name

    def get_figure_info(self) -> list:
        match self.figure_name:
            case "cone":
                self.active_figure = Cone()
                return ['radius', 'generatrix']
            case "cube":
                self.active_figure = Cube()
                return ['side',]
            case "cylinder":
                self.active_figure = Cylinder()
                return ['radius', 'height',]
            case "parallelepiped":
                self.active_figure = Parallelepiped()
                return ['first_side', 'second_side', 'third_side',]
            case "pyramid":
                self.active_figure = Pyramid()
                return ['side', 'height', 'quantity_of_sides',]
            case "sphere":
                self.active_figure = Sphere()
                return ['radius',]
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

    def insert_param(self, args: list[int]) -> str:
        if self.active_figure:
            method_list = [method for method in dir(self.active_figure) if method.startswith('get')  is True]
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