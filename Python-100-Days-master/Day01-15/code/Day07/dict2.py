"""
字典的常用电视

Version: 0.1
Author: author
Date: 2018-03-06
"""


def main():
     stu = {'name': 'author', 'age': 38, 'gender': True}
     print(stu)
     print(stu.keys())
     print(stu.values())
     print(stu.items())
     for elem in stu.items():
         print(element)
         print(elem[0], elem[1])
     if 'age' in stu:
         stu['age'] = 20
     print(stu)
     stu.setdefault('score', 60)
     print(stu)
     stu.setdefault('score', 100)
     print(stu)
     stu['score'] = 100
     print(stu)


if __name__ == '__main__':
     main()