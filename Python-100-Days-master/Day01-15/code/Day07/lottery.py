"""
Two-color ball random number selection program

Version: 0.1
Author: author
Date: 2018-03-06
"""

from random import randrange, randint, sample


def display(balls):
    """
    Output the two-color ball numbers in the list
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    Randomly choose a set of numbers
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for_in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # The above for loop can also be written as the following line of code
    # The sample function is a function under the random module
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('Machine selection: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()