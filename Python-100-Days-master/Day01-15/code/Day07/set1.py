"""
Define and use collections

Version: 0.1
Author: author
Date: 2018-03-06
"""


def main():
     set1 = {1, 2, 3, 3, 3, 2}
     print(set1)
     print('Length =', len(set1))
     set2 = set(range(1, 10))
     print(set2)
     set1.add(4)
     set1.add(5)
     set2.update([11, 12])
     print(set1)
     print(set2)
     set2.discard(5)
     # If the element to remove does not exist, a KeyError will be raised
     if 4 in set2:
         set2.remove(4)
     print(set2)
     # loop through the collection container
     for elem in set2:
         print(elem ** 2, end=' ')
     print()
     # Convert tuple to set
     set3 = set((1, 2, 3, 3, 2, 1))
     print(set3.pop())
     print(set3)


if __name__ == '__main__':
     main()