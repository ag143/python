"""
Use of properties
- Accessor/Modifier/Deleter
- Use __slots__ to restrict attributes

Version: 0.1
Author: author
Date: 2018-03-12
"""


class Car(object):

    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @brand.deleter
    def brand(self):
        del self._brand

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [brand=%s, max speed=%d]' % (self._brand, self._max_speed)


car = Car('QQ', 120)
print(car)
#ValueError
# car.max_speed = -100
car.max_speed = 320
car.brand = "Benz"
# The following code will generate an exception after using the __slots__ attribute limit
# car.current_speed = 80
print(car)
# If a deleter is provided, the following code can be executed
#del car.brand
# property implementation
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
print(Car.brand.fdel)
# Help students understand the previously mentioned concept of wrappers through the above code
# There is a lot of similar syntactic sugar in Python and something like this will follow