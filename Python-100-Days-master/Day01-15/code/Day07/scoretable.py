"""
Student Exam Score Sheet

Version: 0.1
Author: author
Date: 2018-03-06
"""


def main():
     names = ['Guan Yu', 'Zhang Fei', 'Zhao Yun', 'Ma Chao', 'Huang Zhong']
     subjs = ['Chinese', 'Math', 'English']
     scores = [[0] * 3] * 5
     for row, name in enumerate(names):
         print('Please enter the grade of %s' % name)
         for col, subj in enumerate(subjs):
             scores[row][col] = float(input(subj + ': '))
     print(scores)
# for row, name in enumerate(names):
# print('Please enter the grade of %s' % name)
# scores[row] = [None] * len(subjs)
# for col, subj in enumerate(subjs):
# score = float(input(subj + ': '))
# scores[row][col] = score
# print(scores)

if __name__ == '__main__':
     main()