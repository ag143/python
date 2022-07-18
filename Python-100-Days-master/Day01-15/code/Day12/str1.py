"""
String common operations

Version: 0.1
Author: author
Date: 2018-03-19
"""

import pyperclip

# escape character
print('My brother\'s name is \'007\'')
# raw string
print(r'My brother\'s name is \'007\'')

str = 'hello123world'
print('he' in str)
print('her' in str)
# Whether the string contains only letters
print(str.isalpha())
# Whether the string contains only letters and numbers
print(str.isalnum())
# Does the string contain only numbers
print(str.isdecimal())

print(str[0:5].isalpha())
print(str[5:8].isdecimal())

list = ['bright moonlight in front of the bed', 'suspected to be frost on the ground', 'look up at the bright moon', 'look down at the hometown']
print('-'.join(list))
sentence = 'You go your way I will go mine'
words_list = sentence.split()
print(words_list)
email = 'jackfrued@126.com'
print(email)
print(email.strip())
print(email.lstrip())

# Put text into the system clipboard
pyperclip.copy('Tigers don't send cats, you treat me as critically ill')
# Get text from system clipboard
# print(pyperclip.paste())