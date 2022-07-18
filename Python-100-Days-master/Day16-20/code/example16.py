"""
magic method
If you want to put custom objects in set or use as keys in dict
Then you must rewrite the two magic methods __hash__ and __eq__
The former is used to calculate the hash code of the object, and the latter is used to determine whether two objects are the same
Objects with different hash codes must be different objects, but the same hash code is not necessarily the same object (hash code collision)
So when the hash codes are the same, __eq__ is used to determine whether the objects are the same
"""


class Student():
    __slots__ = ('stuid', 'name', 'gender')

    def __init__(self, stuid, name):
        self.stuid = stuid
        self.name = name

    def __hash__(self):
        return hash(self.stuid) + hash(self.name)

    def __eq__(self, other):
        return self.stuid == other.stuid and \
            self.name == other.name

    def __str__(self):
        return f'{self.stuid}: {self.name}'

    def __repr__(self):
        return self.__str__()


class School():

    def __init__(self, name):
        self.name = name
        self.students = {}

    def __setitem__(self, key, student):
        self.students[key] = student

    def __getitem__(self, key):
        return self.students[key]


def main():
    # students = set()
    # students.add(Student(1001, 'King Sledgehammer'))
    # students.add(Student(1001, 'King Sledgehammer'))
    # students.add(Student(1001, 'Bai Yuanfang'))
    # print(len(students))
    # print(students)
    stu = Student(1234, 'Luo Hao')
    stu.gender = 'Male'
    # stu.birth = '1980-11-28'
    print(stu.name, stu.birth)
    school = School('Qianfeng Education')
    school[1001] = Student(1001, 'The King's Hammer')
    school[1002] = Student(1002, 'Bai Yuanfang')
    school[1003] = Student(1003, 'Bai Jie')
    print(school[1002])
    print(school[1003])


if __name__ == '__main__':
    main()