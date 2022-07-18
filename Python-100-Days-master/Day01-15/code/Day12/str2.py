"""
Common operations on strings - methods to implement string inversion

Version: 0.1
Author: author
Date: 2018-03-19
"""

from io import StringIO


def reverse_str1(str):
    return str[::-1]


def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]


def reverse_str3(str):
    # StringIO objects are mutable strings in Python
    # You should not use immutable strings for string concatenation operations because it will generate a lot of useless string objects
    rstr = StringIO()
    str_len = len(str)
    for index in range(str_len - 1, -1, -1):
        rstr.write(str[index])
    return rstr.getvalue()


def reverse_str4(str):
    return ''.join(str[index] for index in range(len(str) - 1, -1, -1))


def reverse_str5(str):
    # process the string into a list
    str_list = list(str)
    str_len = len(str)
    # Use the zip function to combine the two sequences into an iterator that yields a tuple
    # Each time you can just get two subscripts before and after to achieve the exchange of elements
    for i, j in zip(range(str_len // 2), range(str_len - 1, str_len // 2, -1)):
        str_list[i], str_list[j] = str_list[j], str_list[i]
    # Concatenate list elements into strings
    return ''.join(str_list)


if __name__ == '__main__':
    str = 'I love Python'
    print(reverse_str1(str))
    print(str)
    print(reverse_str2(str))
    print(str)
    print(reverse_str3(str))
    print(str)
    print(reverse_str4(str))
    print(str)
    print(reverse_str5(str))
    print(str)