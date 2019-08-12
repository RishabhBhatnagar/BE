import itertools
import operator


dp = lambda *x, **y: __import__('builtins').print(*x, **y)


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
    dp("Input Sequences:", s1, s2)
    return linear_convolution(s1, fold(s2))

auto_correlation = lambda x: cross_correlation(x, x)

dp(
    "Cross Correlated sequence:", 
    cross_correlation(
        [4, 3, 1, 2], 
        [1, 3, 4, 5, 2, 6]
    ), '\n'
)
dp(
    "Auto Correlated sequence:", 
    auto_correlation(
        [1, 4, 2, 0, 3, 5]
    )
)

