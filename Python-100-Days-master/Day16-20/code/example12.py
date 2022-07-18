"""
The three pillars of object orientation: encapsulation, inheritance, polymorphism
Object-Oriented Design Principles: SOLID Principles
Object-Oriented Design Patterns: GoF Design Patterns (Singleton, Factory, Proxy, Strategy, Iterator)
Monthly salary settlement system - department manager 15000 per month, programmer 200 per hour, salesperson 1800 basic salary plus 5% commission on sales
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """Employee (abstract class)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """Pay monthly salary (abstract method)"""
        pass


class Manager(Employee):
    """Department manager"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """programmer"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """Seller"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """Create a factory for employees (factory pattern - decoupling between object consumers and objects through factories)"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """Create employee"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp