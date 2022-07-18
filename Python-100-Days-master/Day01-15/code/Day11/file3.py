"""
write text file
Write prime numbers up to 100 to a file

Version: 0.1
Author: author
Date: 2018-03-13
"""

from math import sqrt


def is_prime(n):
     for factor in range(2, int(sqrt(n)) + 1):
         if n % factor == 0:
             return False
     return True


# try what's different
# with open('prime.txt', 'a') as f:
with open('prime.txt', 'w') as f:
     for num in range(2, 100):
         if is_prime(num):
             f.write(str(num) + '\n')
print('Writing completed!')