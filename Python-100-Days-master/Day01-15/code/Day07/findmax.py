"""
Find the largest or smallest element in a list

Version: 0.1
Author: author
Date: 2018-03-06
"""


def main():
     fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
     # Use the built-in max and min functions directly to find the largest and smallest elements in the list
     # print(max(fruits))
     # print(min(fruits))
     max_value = min_value = fruits[0]
     for index in range(1, len(fruits)):
         if fruits[index] > max_value:
             max_value = fruits[index]
         elif fruits[index] < min_value:
             min_value = fruits[index]
     print('Max:', max_value)
     print('Min:', min_value)


if __name__ == '__main__':
     main()
# Think about what to do if there are two largest elements to find the second largest