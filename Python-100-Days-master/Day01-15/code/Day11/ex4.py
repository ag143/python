"""
Throwing exceptions and exception stack

Version: 0.1
Author: author
Date: 2018-03-13
"""


def f1():
     raise AssertionError('An exception occurred')


def f2():
     f1()


def f3():
     f2()


f3()