"""
Determine whether the input side length can form a triangle
If yes, calculate the perimeter and area of the triangle

Version: 0.1
Author: Luo Hao
Date: 2018-02-28
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
     print('Perimeter: %f' % (a + b + c))
     p = (a + b + c) / 2
     area = math. sqrt(p * (p - a) * (p - b) * (p - c))
     print('Area: %f' % (area))
else:
     print('Cannot form a triangle')