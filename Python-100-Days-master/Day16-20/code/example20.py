"""
Inter-thread communication (shared data) is very simple because the memory of the same process can be shared
Interprocess communication (shared data) is cumbersome because the operating system protects the memory allocated to the process
To achieve multi-process communication, you can usually use system pipes, sockets, and three-party services to achieve
multiprocessing.Queue
daemon thread - daemon thread
Daemons - firewalld/httpd/mysqld
Processes that are not preserved when the system is down - won't prevent the system from being stopped because the process has not finished executing
"""
from threading import Thread
from time import sleep


def output(content):
     while True:
         print(content, end='')


def main():
     Thread(target=output, args=('Ping', ), daemon=True).start()
     Thread(target=output, args=('Pong', ), daemon=True).start()
     sleep(5)
     print('bye!')


if __name__ == '__main__':
     main()