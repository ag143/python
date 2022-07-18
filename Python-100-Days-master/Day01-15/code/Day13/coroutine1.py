"""
Using coroutines - simulate express delivery center

Version: 0.1
Author: author
Date: 2018-03-21
"""

from time import sleep
from random import random


def build_deliver_man(man_id):
     total = 0
     while True:
         total += 1
         print('The courier number %d is ready to take today's order %d.' % (man_id, total))
         pkg = yield
         print('The courier number %d received the package number %s.' % (man_id, pkg))
         sleep(random() * 3)


def package_center(deliver_man, max_per_day):
     num = 1
     deliver_man.send(None)
     # next(deliver_man)
     while num <= max_per_day:
         package_id = 'PKG-%d' % num
         deliver_man.send(package_id)
         num += 1
         sleep(0.1)
     deliver_man.close()
     print('Today's parcel delivery is complete!')


dm = build_deliver_man(1)
package_center(dm, 10)

# Although the two functions have no calling relationship, the function that creates the courier serves as a coroutine to assist the courier center function to complete the task
# Think about what to do if there are multiple couriers