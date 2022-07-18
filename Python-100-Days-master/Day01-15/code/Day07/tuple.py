"""
Definition and use of tuples

Version: 0.1
Author: author
Date: 2018-03-06
"""


def main():
     # define a tuple
     t = ('author', 38, True, 'Chengdu, Sichuan')
     print(t)
     # Get the elements in the tuple
     print(t[0])
     print(t[1])
     print(t[2])
     print(t[3])
     # loop over the values in the tuple
     for member in t:
         print(member)
     # reassign the tuple
     # t[0] = 'The King's Hammer' # TypeError
     # The variable t re-references the new tuple The original tuple is garbage collected
     t = ('Wang Dachui', 20, True, 'Yunnan Kunming')
     print(t)
     # tuple and list conversion
     person = list(t)
     print(person)
     person[0] = 'Bruce Bruce'
     person[1] = 25
     print(person)
     fruits_list = ['apple', 'banana', 'orange']
     fruits_tuple = tuple(fruits_list)
     print(fruits_tuple)
     print(fruits_tuple[1])


if __name__ == '__main__':
     main()