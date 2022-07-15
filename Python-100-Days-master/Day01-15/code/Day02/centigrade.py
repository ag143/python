"""
Convert Fahrenheit to Celsius
F = 1.8C + 32

Version: 0.1
Author: Luo Hao
Date: 2018-02-27
"""

f = float(input('Please enter the temperature in Fahrenheit: '))
c = (f - 32) / 1.8
print('%.1f Fahrenheit = %.1f Celsius' % (f, c))