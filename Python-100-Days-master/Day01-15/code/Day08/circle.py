"""
practise
Build a swimming pool Radius (in meters) is entered when the program is running Build a 3m wide aisle outside the swimming pool
Build a wall on the outside of the aisle. The cost of the aisle is known to be 25 yuan per square meter, and the cost of the wall is 32.5 yuan per meter.
How much is the total cost of the output wall and aisle (accurate to 2 decimal places)

Version: 0.1
Author: author
Date: 2018-03-08
"""

import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius


if __name__ == '__main__':
    radius = float(input('Please enter the radius of the pool: '))
    small = Circle(radius)
    big = Circle(radius + 3)
    print('The cost of the wall is: ￥%.1f yuan' % (big.perimeter * 115))
    print('The cost of the aisle is: ￥%.1f yuan' % ((big.area - small.area) * 65))