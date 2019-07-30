import itertools
import operator

# Copied from exp2
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


def fold(seq):
    return seq[::-1]


def cross_correlation(s1, s2):
    return linear_convolution(s1, fold(s2))

auto_correlation = lambda x: cross_correlation(x, x)

print(cross_correlation([8,9,2,3], [4,3,6]))
