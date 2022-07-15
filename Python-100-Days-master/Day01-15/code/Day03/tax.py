"""
Enter monthly income and five insurances and one housing fund to calculate personal income tax
Explanation: The new personal income tax calculation method has not been enacted at the time of writing this code

Version: 0.1
Author: Luo Hao
Date: 2018-02-28
"""

salary = float(input('This month's salary: '))
insurance = float(input('Five insurances and one housing fund: '))
diff = salary - insurance - 3500
if diff <= 0:
     rate = 0
     deduction = 0
elif diff < 1500:
     rate = 0.03
     deduction = 0
elif diff < 4500:
     rate = 0.1
     deduction = 105
elif diff < 9000:
     rate = 0.2
     deduction = 555
elif diff < 35000:
     rate = 0.25
     deduction = 1005
elif diff < 55000:
     rate = 0.3
     deduction = 2755
elif diff < 80000:
     rate = 0.35
     deduction = 5505
else:
     rate = 0.45
     deduction = 13505
tax = abs(diff * rate - deduction)
print('Individual income tax: ￥%.2f yuan' % tax)
print('Actual income: ￥%.2f yuan' % (diff + 3500 - tax))