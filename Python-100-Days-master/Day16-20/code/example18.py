"""
meta - meta
metadata - data that describes the data - metadata
metaclass - the class that describes the class - metaclass - inherits from type
"""
import threading


class SingletonMeta(type):
    """Custom metaclass"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """President (singleton class)"""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


def main():
    """Main function"""
    p1 = President('Trump', 'America')
    p2 = President('Obama', 'America')
    p3 = President.__call__('Clinton', 'United States')
    print(p1 == p2)
    print(p1 == p3)
    print(p1, p2, p3, sep='\n')


if __name__ == '__main__':
    main()