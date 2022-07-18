"""
Craps gambling game
Player rolls two dice If the first roll is 7 or 11, the player wins
If it rolls out 2 points 3 points 12 points, the banker wins, otherwise the game continues
Player asks for dice again If 7 is rolled, the banker wins
If the first roll is rolled, the player wins
Otherwise the game continues and the player continues to roll the dice
When the player enters the game, there is a bet of 1,000 yuan, and the game is over

Version: 0.1
Author: author
Date: 2018-03-02
"""
from random import randint

money = 1000
while money > 0:
    print('Your total assets are:', money)
    needs_go_on = False
    while True:
        debt = int(input('Please bet: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('The player shakes the %d point' % first)
    if first == 7 or first == 11:
        print('Player wins!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('Banker wins!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('The player shakes the %d point' % current)
        if current == 7:
            print('Banker wins')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('Player wins')
            money += debt
            needs_go_on = False

print('You are broke, game over!')