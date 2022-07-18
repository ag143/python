"""
Find the number of all daffodils between 100 and 999
The daffodil number is the sum of the cubes of each position equal to the number itself
For example: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: author
Date: 2018-03-02
"""

for num in range(100, 1000):
     low = num % 10
     mid = num // 10 % 10
     high = num // 100
     if num == low ** 3 + mid ** 3 + high ** 3:
         print(num)