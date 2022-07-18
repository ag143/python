"""
Output multiplication formula table (nine-nine table)

Version: 0.1
Author: author
Date: 2018-03-02
"""

for i in range(1, 10):
     for j in range(1, i + 1):
         print('%d*%d=%d' % (i, j, i * j), end='\t')
     print()