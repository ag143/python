"""
Enter student test scores to calculate average score

Version: 0.1
Author: author
Date: 2018-03-06
"""


def main():
     number = int(input('Please enter the number of students: '))
     names = [None] * number
     scores = [None] * number
     for index in range(len(names)):
         names[index] = input('Please enter the name of the %dth student: ' % (index + 1))
         scores[index] = float(input('Please enter the score of the %d student: ' % (index + 1)))
     total = 0
     for index in range(len(names)):
         print('%s: %.1f score' % (names[index], scores[index]))
         total += scores[index]
     print('The average grade is: %.1f points' % (total / number))


if __name__ == '__main__':
     main()