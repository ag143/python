"""
Multiple Inheritance - A class has two or more parent classes
MRO - Method Resolution Order - Method Resolution Order
When diamond inheritance (diamond inheritance) occurs, which parent class method does the subclass inherit from?
Python 2.x - Depth First Search
Python 3.x - C3 Algorithm - Similar to Breadth First Search
"""
classA():

    def say_hello(self):
        print('Hello, A')


class B(A):
    pass


class C(A):

    def say_hello(self):
        print('Hello, C')


class D(B, C):
    pass


class SetOnceMappingMixin():
    """Custom mixin class"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """Custom Dictionary"""
    pass


def main():
    print(D.mro())
    # print(D.__mro__)
    D().say_hello()
    print(SetOnceDict.__mro__)
    my_dict= SetOnceDict()
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'


if __name__ == '__main__':
    main()