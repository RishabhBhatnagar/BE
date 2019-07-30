import itertools
import operator
from collections import deque


DEBUG = True
dp = lambda *x, **y: __import__('builtins').print(*x, **y) if DEBUG else lambda *x, **y: None


def pad(seq, n, e=0):
    seq.extend(itertools.repeat(e, n - len(seq)))
    return seq


def linear_convolution(s1, s2):
    # s1, s2 are the sequences with origin at 0th element.
    # s1, s2 : unexhaustible iterable.
    n1, n2 = map(len, [s1, s2])
    dp("Input Sequences:", s1, s2)
    x3 = list(itertools.repeat(0, n1 + n2 - 1))
    p = tuple(itertools.starmap(operator.mul, itertools.product(s1, s2)))
    for i in range(n1):
        for j in range(n2):
            x3[i + j] += p[n2 * i + j]
    return x3


def circular_convolution(s1, s2):
    dp("Input Sequences:", s1, s2)
    n = max(map(len, [s1, s2]))
    s1, s2 = pad(s1, n), pad(s2, n)
    matrix = []
    q = deque(s1[::-1])
    for _ in itertools.repeat(None, n):
        q.rotate(1)
        matrix.append(list(q))
    dp("Matrix:", *matrix, sep='\n')
    return [sum(itertools.starmap(operator.mul, zip(row, s2))) for row in matrix]


def linear_circular(s1, s2):
    dp("Initial Input Sequences:", s1, s2)
    n = sum(map(len, [s1, s2])) - 1
    s1, s2 = pad(s1, n), pad(s2, n)
    return circular_convolution(s1, s2)


dp("Linear Convoluted Sequence:", linear_convolution([2, 3, -1, 4], [-1, 2 ,1, -1]), '\n')
dp("Circular Convoluted Sequence:", circular_convolution([1, 2, 3, 4], [7, -2, 1, 3]), '\n')
dp("Linear Using Circular Convolution:", linear_circular([3, 2, 4, -1], [2, 1, -1, 0, 3]))


'''
OUPUT:
Input Sequences: [2, 3, -1, 4] [-1, 2, 1, -1]
Linear Convoluted Sequence: [-2, 1, 9, -5, 4, 5, -4] 

Input Sequences: [1, 2, 3, 4] [7, -2, 1, 3]
Matrix:
[1, 4, 3, 2]
[2, 1, 4, 3]
[3, 2, 1, 4]
[4, 3, 2, 1]
Circular Convoluted Sequence: [8, 25, 30, 27] 

Initial Input Sequences: [3, 2, 4, -1] [2, 1, -1, 0, 3]
Input Sequences: [3, 2, 4, -1, 0, 0, 0, 0] [2, 1, -1, 0, 3, 0, 0, 0]
Matrix:
[3, 0, 0, 0, 0, -1, 4, 2]
[2, 3, 0, 0, 0, 0, -1, 4]
[4, 2, 3, 0, 0, 0, 0, -1]
[-1, 4, 2, 3, 0, 0, 0, 0]
[0, -1, 4, 2, 3, 0, 0, 0]
[0, 0, -1, 4, 2, 3, 0, 0]
[0, 0, 0, -1, 4, 2, 3, 0]
[0, 0, 0, 0, -1, 4, 2, 3]
Linear Using Circular Convolution: [6, 7, 7, 0, 4, 7, 12, -3]
'''

