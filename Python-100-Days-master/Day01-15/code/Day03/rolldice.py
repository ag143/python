"""
Roll the dice to decide what to do

Version: 0.1
Author: Luo Hao
Date: 2018-02-28
"""
from random import randint

face = randint(1, 6)
if face == 1:
     result = 'clicker'
elif face == 2:
     result = 'dance'
elif face == 3:
     result = 'Learn to bark'
elif face == 4:
     result = 'Do push-ups'
elif face == 5:
     result = 'recite the tongue twister'
else:
     result = 'tell a bad joke'
print(result)