"""
100% grades to grades grades
Above 90 points, output A
80 to 89 points, output B
70 to 79 points, output C
60 to 69 points, output D
Below 60 points, output E

Version: 0.1
Author: Luo Hao
Date: 2018-02-28
"""

score = float(input('Please enter the score: '))
if score >= 90:
     grade = 'A'
elif score >= 80:
     grade = 'B'
elif score >= 70:
     grade = 'C'
elif score >= 60:
     grade = 'D'
else:
     grade = 'E'
print('The corresponding grade is:', grade)