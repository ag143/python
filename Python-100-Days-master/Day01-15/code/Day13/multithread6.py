"""
Multiple threads share data - lock case

Version: 0.1
Author: author
Date: 2018-03-20
"""

import time
import threading


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = threading.Lock()

    def deposit(self, money):
        # After the lock is obtained, the code can continue to execute
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            time.sleep(0.01)
            self._balance = new_balance
        finally:
            # Remember to release the lock after the operation is complete
            self._lock.release()

    @property
    def balance(self):
        return self._balance


if __name__ == '__main__':
    account = Account()
    # Create a thread for 100 deposits to deposit money into the same account
    for _ in range(100):
        threading.Thread(target=account.deposit, args=(1,)).start()
    # Wait for all deposit threads to finish executing
    time.sleep(2)
    print('The account balance is: ￥%d yuan' % account.balance)

# Think about why the result is not the 100 yuan we expected