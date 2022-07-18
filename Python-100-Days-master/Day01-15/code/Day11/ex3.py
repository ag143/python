"""
Exception Mechanism - states that may occur while the handler is running

Version: 0.1
Author: author
Date: 2018-03-13
"""

import time
import sys

filename = input('Please enter the filename: ')
try:
     with open(filename) as f:
         lines = f.readlines()
except FileNotFoundError as msg:
     print('Unable to open file:', filename)
     print(msg)
except UnicodeDecodeError as msg:
     print('Non-text files cannot be decoded')
     sys.exit()
else:
     for line in lines:
         print(line.rstrip())
         time.sleep(0.5)
finally:
     # This is the best place to do the aftermath
     print('I will execute no matter what happens')