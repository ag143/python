"""
Working with coroutines - view the state of a coroutine

Version: 0.1
Author: author
Date: 2018-03-21
"""

from time import sleep
from inspect import getgeneratorstate


def build_deliver_man(man_id):
    total = 0
    while True:
        total += 1
        print('The courier number %d is ready to take today's order %d.' % (man_id, total))
        pkg = yield
        print('The courier number %d received the package number %s.' % (man_id, pkg))
        sleep(0.5)


def package_center(deliver_man, max_per_day):
    num = 1
    # Create state (GEN_CREATED) - waiting to start execution
    print(getgeneratorstate(deliver_man))
    deliver_man.send(None)
    # Suspended state (GEN_SUSPENDED) - Suspended at yield expression
    print(getgeneratorstate(deliver_man))
    # next(deliver_man)
    while num <= max_per_day:
        package_id = 'PKG-%d' % num
        deliver_man.send(package_id)
        num += 1
    deliver_man.close()
    # end state (GEN_CLOSED) - execution completed
    print(getgeneratorstate(deliver_man))
    print('Today's parcel delivery is complete!')


dm = build_deliver_man(1)
package_center(dm, 10)