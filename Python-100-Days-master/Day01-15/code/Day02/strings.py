"""
String common operations

Version: 0.1
Author: Luo Hao
Date: 2018-02-27
"""

str1 = 'hello, world!'
print('The length of the string is:', len(str1))
print('The first letter of the word is capitalized: ', str1.title())
print('The string is uppercase: ', str1.upper())
# str1 = str1.upper()
print('is the string uppercase: ', str1.isupper())
print('Does the string start with hello: ', str1.startswith('hello'))
print('Does the string end with hello: ', str1.endswith('hello'))
print('Does the string start with an exclamation mark: ', str1.startswith('!'))
print('Does the string end with an exclamation mark: ', str1.endswith('!'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)