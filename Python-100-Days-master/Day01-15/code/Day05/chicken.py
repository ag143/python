"""
Solve the "Hundred Money Hundred Chicken" problem
1 rooster, 5 yuan, 1 hen, 3 yuan, 3 chicks, 1 yuan, 100 chickens for 100 yuan
Ask how many roosters, hens and chicks each have

Version: 0.1
Author: author
Date: 2018-03-02
"""

for x in range(0, 20):
     for y in range(0, 33):
         z = 100 - x - y
         if 5 * x + 3 * y + z / 3 == 100:
             print('rooster: %d, hen: %d, chick: %d' % (x, y, z))