"""
Enter the radius to calculate the circumference and area of the circle

Version: 0.1
Author: Luo Hao
Date: 2018-02-27
"""
import math

radius = float(input('Please enter the radius of the circle: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('Perimeter: %.2f' % perimeter)
print('Area: %.2f' % area)