"""
Exception Mechanism - states that may occur while the handler is running

Version: 0.1
Author: author
Date: 2018-03-13
"""

input_again = True
while input_again:
     try:
         a = int(input('a = '))
         b = int(input('b = '))
         print('%d / %d = %f' % (a, b, a / b))
         input_again = False
     except ValueError:
         print('Please enter an integer')
     except ZeroDivisionError:
         print('Divisor cannot be 0')
# Handling exceptions so that the code does not crash due to exceptions is one aspect
# More importantly, the code can recover from the exception by handling the exception