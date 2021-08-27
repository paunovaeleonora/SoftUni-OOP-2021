from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class TreeModelling(ABC):
    @abstractmethod
    def model_3d(self, shape):
        pass


class Rectangle(Shape):
    def draw(self):
        print('Drawing rectangle')


class Circle(Shape):
    def draw(self):
        print('Drawing circle')