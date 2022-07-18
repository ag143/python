"""
Verify whether the entered user name and QQ number are valid and give the corresponding prompt information

Require:
Username must consist of letters, numbers or underscores and must be between 6 and 20 characters in length
The QQ number is a number from 5 to 12 and the first position cannot be 0
"""

import re


def main():
     username = input('Please enter username: ')
     qq = input('Please enter the QQ number: ')
     m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
     if not m1:
         print('Please enter a valid username.')
     m2 = re.match(r'^[1-9]\d{4,11}$', qq)
     if not m2:
         print('Please enter a valid QQ number.')
     if m1 and m2:
         print('The information you entered is valid!')


if __name__ == '__main__':
     main()