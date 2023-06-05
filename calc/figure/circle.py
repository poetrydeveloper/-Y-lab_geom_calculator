import math

from calc.figure.figure import Figure


class Circle(Figure):
    def __init__(self, radius=0, diameter=0, area=0, circle=0):
        self.__info = ["radius", "diameter", "area", "circle"]
        self.radius = radius
        self.diameter = diameter
        self.area = area
        self.circle = circle

        self.revision()

    def revision(self):
        if self.radius != 0:
            if self.diameter == 0: self.calc_diameter()
            if self.area == 0: self.calc_area()
            if self.circle == 0: self.calc_circle()
        else:
            print("When creating a circle, you need to know at least the radius")

    @property
    def info(self):
        return self.__info
    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.diameter

    def get_area(self):
        return self.area

    def get_circle(self):
        return self.circle

    def calc_circle(self):
        self.circle =  2 * math.pi * self.radius


    def calc_area(self):
        self.area = math.pi * (self.radius**2)

    def calc_diameter(self):
        self.diameter = 2 * self.radius

