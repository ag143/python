"""
Define and use lists
- Access elements with subscripts
- add elements
- remove element

Version: 0.1
Author: author
Date: 2018-03-06
"""


def main():
     fruits = ['grape', '@pple', 'strawberry', 'waxberry']
     print(fruits)
     # access element by subscript
     print(fruits[0])
     print(fruits[1])
     print(fruits[-1])
     print(fruits[-2])
     # print(fruits[-5]) # IndexError
     # print(fruits[4]) # IndexError
     fruits[1] = 'apple'
     print(fruits)
     # add element
     fruits.append('pitaya')
     fruits.insert(0, 'banana')
     print(fruits)
     # delete element
     del fruits[1]
     fruits.pop()
     fruits.pop(0)
     fruits.remove('apple')
     print(fruits)


if __name__ == '__main__':
     main()