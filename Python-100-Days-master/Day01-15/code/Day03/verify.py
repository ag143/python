"""
User authentication

Version: 0.1
Author: Luo Hao
Date: 2018-02-28
"""
# import getpass
# from getpass import getpass
# from getpass import *

username = input('Please enter username: ')
password = input('Please enter the password: ')
# There is no echo in the terminal when entering the password
# password = getpass.getpass('Please enter password: ')
if username == 'admin' and password == '123456':
     print('Authentication successful!')
else:
     print('Authentication failed!')
