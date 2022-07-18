"""
Create a process to call other programs

Version: 0.1
Author: author
Date: 2018-03-20
"""

import subprocess
import sys

def main():
     # Get command line arguments through sys.argv
     if len(sys.argv) > 1:
         # The first command-line argument is the program itself, so start with the second
         for index in range(1, len(sys.argv)):
             try:
                 # Start the subprocess through the call function of the subprocess module
                 status = subprocess.call(sys.argv[index])
             except FileNotFoundError:
                 print('Cannot execute %s command' % sys.argv[index])
     else:
         print('Please use command line parameters to specify the process to execute')


if __name__ == '__main__':
     main()