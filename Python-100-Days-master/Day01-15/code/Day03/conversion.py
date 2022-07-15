"""
Swap between imperial inches and metric centimeters

Version: 0.1
Author: Luo Hao
Date: 2018-02-28
"""

value = float(input('Please enter the length: '))
unit = input('Please enter the unit: ')
if unit == 'in' or unit == 'inch':
     print('%f inches = %f cm' % (value, value * 2.54))
elif unit == 'cm' or unit == 'cm':
     print('%f cm = %f inches' % (value, value / 2.54))
else:
     print('Please enter a valid unit')