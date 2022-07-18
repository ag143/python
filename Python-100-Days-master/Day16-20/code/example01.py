"""
Search - Sequential Search and Binary Search
Algorithms: Methods of Solving Problems (Steps)
There are two main indicators for evaluating the quality of an algorithm: asymptotic time complexity and asymptotic space complexity. Usually, it is difficult for an algorithm to achieve low time complexity and space complexity (because time and space are irreconcilable). contradiction)
Representing asymptotic time complexity is usually done using Big O notation
O(c): Constant Time Complexity - Hash Storage / Bloom Filter
O(log_2 n): Logarithmic Time Complexity - Find in Half
O(n): Linear Time Complexity - Sequential Search
O(n * log_2 n): - log-linear time complexity - advanced sorting algorithms (merge sort, quick sort)
O(n**2): Squared Time Complexity - Simple Sorting Algorithms (Bubble Sort, Selection Sort, Insertion Sort)
O(n**3): Cubic Time Complexity - Floyd's Algorithm / Matrix Multiplication
Also known as polynomial time complexity
O(2**n): Geometric series time complexity - Tower of Hanoi
O(3**n): geometric series time complexity
Also known as exponential time complexity
O(n!): Factorial Time Complexity - Traveling Dealer Problem - NP
"""
from math import log2, factorial
from matplotlib import pyplot

import numpy


def seq_search(items: list, elem) -> int:
    """Search order"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


def bin_search(items, elem):
    """Binary search"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def main():
    """Main function (program entry)"""
    num = 6
    styles = ['r-.', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
    legends = ['log', 'linear', 'linear-log', 'square', 'cubic', 'geometric series', 'factorial']
    x_data = [x for x in range(1, num + 1)]
    y_data1 = [log2(y) for y in range(1, num + 1)]
    y_data2 = [y for y in range(1, num + 1)]
    y_data3 = [y * log2(y) for y in range(1, num + 1)]
    y_data4 = [y ** 2 for y in range(1, num + 1)]
    y_data5 = [y ** 3 for y in range(1, num + 1)]
    y_data6 = [3 ** y for y in range(1, num + 1)]
    y_data7 = [factorial(y) for y in range(1, num + 1)]
    y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, styles[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(1, 7, step=1))
    pyplot.yticks(numpy.arange(0, 751, step=50))
    pyplot.show()


if __name__ == '__main__':
    main()