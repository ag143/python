"""
generate list
- Create a list of numbers with range
- Generate expressions
- Builder

Version: 0.1
Author: author
Date: 2018-03-06
"""


# Generator for generating Fibonacci sequences
def fib(n):
     a, b = 0, 1
     for _ in range(n):
         a, b = b, a + b
         yield a


def main():
     # create a list of values using range
     list1 = list(range(1, 11))
     print(list1)
     # generate expression
     list2 = [x * x for x in range(1, 11)]
     print(list2)
     list3 = [m + n for m in 'ABCDEFG' for n in '12345']
     print(list3)
     print(len(list3))
     # generator (saves space but takes time to generate next element)
     gen = (m + n for m in 'ABCDEFG' for n in '12345')
     print(gen)
     for elem in gen:
         print(elem, end=' ')
     print()
     gen = fib(20)
     print(gen)
     for elem in gen:
         print(elem, end=' ')
     print()


if __name__ == '__main__':
     main()