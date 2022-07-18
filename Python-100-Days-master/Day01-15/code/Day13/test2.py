import time
from threading import Thread, Lock


class Account(object):

    def __init__(self, balance=0):
        self._balance = balance
        self._lock = Lock()

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        # When multiple threads access a resource at the same time, the state of the resource may be wrong due to competition for resources
        # Resources accessed by multiple threads are usually called critical resources. Access to critical resources needs to be protected
        if money > 0:
            self._lock.acquire()
            try:
                new_balance = self._balance + money
                time.sleep(0.01)
                self._balance = new_balance
            finally:
                self._lock.release()


class AddMoneyThread(Thread):

    def __init__(self, account):
        super().__init__()
        self._account = account

    def run(self):
        self._account.deposit(1)


def main():
    account = Account(1000)
    tlist = []
    for _ in range(100):
        t = AddMoneyThread(account)
        tlist.append(t)
        t.start()
    for t in tlist:
        t.join()
    print('Account balance: %d yuan' % account.balance)


if __name__ == '__main__':
    main()