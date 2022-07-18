"""
multiple inheritance
- Diamond Inheritance (Diamond Inheritance)
- C3 algorithm (algorithm that replaces DFS)

Version: 0.1
Author: author
Date: 2018-03-12
"""


class A(object):

     def foo(self):
         print('foo of A')


class B(A):
     pass


class C(A):

     def foo(self):
         print('foo fo C')


class D(B, C):
     pass


class E(D):

     def foo(self):
         print('foo in E')
         super().foo()
         super(B, self).foo()
         super(C, self).foo()


if __name__ == '__main__':
     d = D()
     d.foo()
     e = E()
     e.foo()