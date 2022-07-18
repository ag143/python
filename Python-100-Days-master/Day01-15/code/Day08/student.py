"""
Defining and Using Student Classes

Version: 0.1
Author: author
Date: 2018-03-08
"""


def _foo():
    print('test')


class Student(object):

    # __init__ is a special method used to initialize objects when they are created
    # Through this method, we can bind the two properties of name and age to the student object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s is studying %s.' % (self.name, course_name))

    # PEP 8 requires identifier names to be in all lowercase with multiple words concatenated with underscores
    # But many programmers and companies prefer to use CamelCase (CamelCase)
    def watch_av(self):
        if self.age < 18:
            print('%s can only watch "Bears".' % self.name)
        else:
            print('%s is watching the Big Island movie.' % self.name)


def main():
    stu1 = Student('author', 38)
    stu1.study('Python programming')
    stu1.watch_av()
    stu2 = Student('The King's Hammer', 15)
    stu2.study('ideological and moral')
    stu2.watch_av()


if __name__ == '__main__':
    main()