"""
Read CSV file

Version: 0.1
Author: author
Date: 2018-03-13
"""

import csv

filename = 'example.csv'

try:
     with open(filename) as f:
         reader = csv.reader(f)
         data = list(reader)
except FileNotFoundError:
     print('Unable to open file:', filename)
else:
     for item in data:
         print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))