"""
Application of instance methods and class methods

Version: 0.1
Author: author
Date: 2018-03-12
"""

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # static method
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b

    # instance method
    def perimeter(self):
        return self._a + self._b + self._c

    # instance method
    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


if __name__ == '__main__':
    # Split the string into a list using the split method of the string
    # Then use the map function to map each string in the list into decimals
    a, b, c = map(float, input('Please input three sides: ').split())
    # First determine whether three sides of a given length can form a triangle
    # Create a triangle object if you can
    if Triangle.is_valid(a, b, c):
        tri = Triangle(a, b, c)
        print('Perimeter:', tri.perimeter())
        print('Area:', tri.area())
        # If you pass an object as a method parameter, you can also call instance methods through the class
        # print('Perimeter:', Triangle.perimeter(tri))
        # print('Area:', Triangle.area(tri))
        # Look at the following code to know that the two are essentially the same
        # print(type(tri.perimeter))
        # print(type(Triangle.perimeter))
    else:
        print('Cannot form a triangle.')