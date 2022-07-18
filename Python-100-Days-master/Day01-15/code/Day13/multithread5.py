"""
Multiple threads share data - no lock case

Version: 0.1
Author: author
Date: 2018-03-20
"""

from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # Obtain the lock before executing subsequent code
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # This code is placed in finally to ensure that the operation of releasing the lock must be executed
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # Create a thread for 100 deposits to deposit money into the same account
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # Wait for all deposit threads to finish executing ∫
    for t in threads:
        t.join()
    print('The account balance is: ￥%d yuan' % account.balance)


if __name__ == '__main__':
    main()