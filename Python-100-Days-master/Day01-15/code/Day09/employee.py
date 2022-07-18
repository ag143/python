"""
abstract class / method overriding / polymorphism
Implementing a payroll system The company has three types of employees
- The fixed monthly salary of the department manager is 12,000 yuan/month
- Programmers are paid 100 yuan per hour based on the number of hours worked in this month
- Salesperson's basic salary of 1,500 yuan/month plus a 5% commission on this month's sales
Enter employee information Output monthly salary information for each employee

Version: 0.1
Author: author
Date: 2018-03-12
"""

from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    # Think about it: what happens if you don't define a constructor
    def __init__(self, name):
        # Think about it: what happens if you don't call the superclass constructor
        super().__init__(name)

    def get_salary(self):
        return 12000


class Programmer(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):
        return 100 * self._working_hour


class Salesman(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1500 + self._sales * 0.05


if __name__ == '__main__':
    emps = [Manager('Wu Zetian'), Programmer('Di Renjie'), Salesman('Bai Yuanfang')]
    for emp in emps:
        if isinstance(emp, Programmer):
            working_hour = int(input('Please enter %s working time this month: ' % emp.name))
            emp.set_working_hour(working_hour)
        elif isinstance(emp, Salesman):
            sales = float(input('Please enter %s sales this month: ' % emp.name))
            emp.set_sales(sales)
        print('%s monthly salary is: ￥%.2f yuan' % (emp.name, emp.get_salary()))