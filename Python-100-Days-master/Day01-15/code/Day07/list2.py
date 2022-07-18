"""
List common operations
- List connection
- get length
- traverse the list
- List slices
- List sorting
- List inversion
- find element

Version: 0.1
Author: author
Date: 2018-03-06
"""


def main():
     fruits = ['grape', 'apple', 'strawberry', 'waxberry']
     fruits += ['pitaya', 'pear', 'mango']
     # loop through the list elements
     for fruit in fruits:
         print(fruit.title(), end=' ')
     print()
     # list slice
     fruits2 = fruits[1:4]
     print(fruits2)
     # fruit3 = fruits # No copy list but new reference created
     fruits3 = fruits[:]
     print(fruits3)
     fruits4 = fruits[-3:-1]
     print(fruits4)
     fruits5 = fruits[::-1]
     print(fruits5)


if __name__ == '__main__':
     main()