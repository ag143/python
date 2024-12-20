"""
Output 10 rows of Yanghui's triangle - nth power expansion coefficient of binomial
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
... ...


Version: 0.1
Author: author
Date: 2018-03-06
"""


def main():
     num = int(input('Number of rows: '))
     yh = [[]] * num
     for row in range(len(yh)):
         yh[row] = [None] * (row + 1)
         for col in range(len(yh[row])):
             if col == 0 or col == row:
                 yh[row][col] = 1
             else:
                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
             print(yh[row][col], end='\t')
         print()


if __name__ == '__main__':
     main()