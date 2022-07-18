#!/usr/bin/python3
# coding: utf-8
from random import randint


def main():
     answer = randint(1, 100)
     while True:
         number = int(input('Please input: '))
         if number < answer:
             print('bigger')
         elif number > answer:
             print('smaller')
         else:
             print('Congratulations on your guess!')
             break


if __name__ == '__main__':
     main()