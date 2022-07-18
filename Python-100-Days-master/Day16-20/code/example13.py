from example12 import EmployeeFactory


def main():
     """Main function"""
     emps = [
         EmployeeFactory.create('M', 'Cao Cao'),
         EmployeeFactory.create('P', 'Xun Yu', 120),
         EmployeeFactory.create('P', 'Guo Jia', 85),
         EmployeeFactory.create('S', 'Dianwei', 123000),
     ]
     for emp in emps:
         print('%s: %.2f yuan' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
     main()