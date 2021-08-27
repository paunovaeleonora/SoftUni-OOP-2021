from abc import abstractmethod, ABC
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        return None
    @abstractmethod
    def calculate_perimeter(self):
        return None


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return pi * self._radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self._radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self._height = height
        self._width = width

    def calculate_area(self):
        return self._height * self._width

    def calculate_perimeter(self):
        return 2 * (self._height + self._width)

# circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())
# rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())