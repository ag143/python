"""
Read data from text file

Version: 0.1
Author: author
Date: 2018-03-13
"""

import time


def main():
     # Read the entire file content at once
     with open('tooak.txt', 'r', encoding='utf-8') as f:
         print(f.read())

     # Read line by line through a for-in loop
     with open('To Oak.txt', mode='r') as f:
         for line in f:
             print(line, end='')
             time.sleep(0.5)
     print()

     # Read the file into a list line by line
     with open('to oak.txt') as f:
         lines = f.readlines()
     print(lines)
    

if __name__ == '__main__':
     main()