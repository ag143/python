"""
Read the pi file to determine whether it contains your own birthday

Version: 0.1
Author: author
Date: 2018-03-13
"""

birth = input('Please enter your birthday: ')
with open('pi_million_digits.txt') as f:
     lines = f.readlines()
     pi_string = ''
     for line in lines:
         pi_string += line.strip()
     if birth in pi_string:
         print('Bingo!!!')