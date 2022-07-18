"""
Defining and Using the Rectangle Class

Version: 0.1
Author: author
Date: 2018-03-08
"""


class Rect(object):
     """Rectangle class"""

     def __init__(self, width=0, height=0):
         """Initialization method"""
         self.__width = width
         self.__height = height

     def perimeter(self):
         """Calculate perimeter"""
         return (self.__width + self.__height) * 2

     def area(self):
         """Calculate area"""
         return self.__width * self.__height

     def __str__(self):
         """String expression of rectangle object"""
         return 'Rectangle[%f,%f]' % (self.__width, self.__height)

     def __del__(self):
         """Destructor"""
         print('Destroy the rectangle object')


if __name__ == '__main__':
     rect1 = Rect()
     print(rect1)
     print(rect1.perimeter())
     print(rect1.area())
     rect2 = Rect(3.5, 4.5)
     print(rect2)
     print(rect2.perimeter())
     print(rect2.area())