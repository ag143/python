"""
inherited application
- abstract class
- abstract methods
- method overriding
- Polymorphism

Version: 0.1
Author: author
Date: 2018-03-12
"""

from abc import ABCMeta, abstractmethod
from math import pi


class Shape(object, metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def perimeter(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return 'I am a circle'


class Rect(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __str__(self):
        return 'I am a rectangle'


if __name__ == '__main__':
    shapes = [Circle(5), Circle(3.2), Rect(3.2, 6.3)]
    for shape in shapes:
        print(shape)
        print('perimeter:', shape.perimeter())
        print('Area:', shape.area())