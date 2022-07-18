"""
multiple inheritance
- Through multiple inheritance, an object of a class can have multiple capabilities
- In this way, when designing classes, you can avoid designing too many levels of complex inheritance relationships

Version: 0.1
Author: author
Date: 2018-03-12
"""


class Father(object):

    def __init__(self, name):
        self._name = name

    def gamble(self):
        print('%s is playing mahjong.' % self._name)

    def eat(self):
        print('%s is eating and drinking.' % self._name)


class Monk(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s is eating fast.' % self._name)

    def chant(self):
        print('%s is chanting.' % self._name)


class Musician(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s is chewing slowly.' % self._name)

    def play_piano(self):
        print('%s is playing the piano.' % self._name)


# Try the code below to see the difference
# class Son(Monk, Father, Musician):
# class Son(Musician, Father, Monk):


class Son(Father, Monk, Musician):

    def __init__(self, name):
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Musician.__init__(self, name)


son = Son('The King's Hammer')
son.gamble()
# Call the eat method inherited from Father
son.eat()
son.chant()
son.play_piano()