# Плоские фигуры: круг, квадрат, прямоугольник, треугольник, трапеция, ромб.
#
# Объемные фигуры: сфера, куб, параллелепипед, пирамида, цилиндр, конус.

# плоские
# круг
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass
