"""
Use while loop to achieve the sum of even numbers between 1 and 100

Version: 0.1
Author: Luo Hao
Date: 2018-03-01
"""

sum, num = 0, 2
while num <= 100:
     sum += num
     num += 2
print(sum)