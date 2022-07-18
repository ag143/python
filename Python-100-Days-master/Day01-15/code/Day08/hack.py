"""
Another way to create a class

Version: 0.1
Author: author
Date: 2018-03-08
"""


def bar(self, name):
     self._name = name


def foo(self, course_name):
     print('%s is studying %s.' % (self._name, course_name))


def main():
     Student = type('Student', (object,), dict(__init__=bar, study=foo))
     stu1 = Student('author')
     stu1.study('Python programming')


if __name__ == '__main__':
     main()