"""
Enter the year if it is a leap year, output True, otherwise output False

Version: 0.1
Author: Luo Hao
Date: 2018-02-27
"""

year = int(input('Please enter the year: '))
# If the code is too long to be written on one line and it is not easy to read, you can use \ or () to wrap the line
is_leap = (year % 4 == 0 and year % 100 != 0 or
            year % 400 == 0)
print(is_leap)