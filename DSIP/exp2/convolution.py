import itertools
import operator
from collections import deque


def pad(seq, n, e=0):
    seq.extend(itertools.repeat(e, n - len(seq)))
    return seq


def linear_convolution(s1, s2):
    # s1, s2 are the sequences with origin at 0th element.
    # s1, s2 : unexhaustible iterable.
    n1, n2 = map(len, [s1, s2])
    x3 = list(itertools.repeat(0, n1 + n2 - 1))
    p = tuple(itertools.starmap(operator.mul, itertools.product(s1, s2)))
    for i in range(n1):
        for j in range(n2):
            x3[i + j] += p[n2 * i + j]
    return x3


def circular_convolution(s1, s2):
    n = max(map(len, [s1, s2]))
    s1, s2 = pad(s1, n), pad(s2, n)
    matrix = []
    q = deque(s1[::-1])
    for _ in itertools.repeat(None, n):
        q.rotate(1)
        matrix.append(list(q))
    return [sum(itertools.starmap(operator.mul, zip(row, s2))) for row in matrix]

def linear_circular(s1, s2):
    n = sum(map(len, [s1, s2])) - 1
    s1, s2 = pad(s1, n), pad(s2, n)
    return circular_convolution(s1, s2)

