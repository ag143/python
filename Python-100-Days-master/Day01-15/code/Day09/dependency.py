"""
Dependencies between objects and operator overloading

Version: 0.1
Author: author
Date: 2018-03-12
"""


class Car(object):

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand

    def accelerate(self, delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return '%s current speed%d' % (self._brand, self._current_speed)


class Student(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    # There is a dependency between the student and the car - the student uses the car
    def drive(self, car):
        print('%s drove %s happily on the road to the West' % (self._name, car._brand))
        car.accelerate(30)
        print(car)
        car.accelerate(50)
        print(car)
        car.accelerate(50)
        print(car)

    def study(self, course_name):
        print('%s is studying %s.' % (self._name, course_name))

    def watch_av(self):
        if self._age < 18:
            print('%s can only watch "Bears".' % self._name)
        else:
            print('%s is watching an island love action movie.' % self._name)

    # Overload the greater than (>) operator
    def __gt__(self, other):
        return self._age > other._age

    # Overload the less than (<) operator
    def __lt__(self, other):
        return self._age < other._age


if __name__ == '__main__':
    stu1 = Student('author', 38)
    stu1.study('Python programming')
    stu1.watch_av()
    stu2 = Student('The King's Hammer', 15)
    stu2.study('ideological and moral')
    stu2.watch_av()
    car = Car('QQ', 120)
    stu2.drive(car)
    print(stu1 > stu2)
    print(stu1 < stu2)