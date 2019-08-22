import math


def euler_pow(x):
    # returns: e ** (xj)
    return math.cos(x) + 1j * math.sin(x)


def fft(x):
    n = len(x)
    if n == 1:
        return x
    w_n = euler_pow(2 * math.pi / n)
    w = 1
    y_0, y_1 = fft(x[0::2]), fft(x[1::2])
    ans = [0 for i in range(n)]
    for k in range((n >> 1)):
        t = w * y_1[k]
        ans[k] = y_0[k] + t
        ans[k + (n >> 1)] = y_0[k] - t
        w = w * w_n
    return ans


def ifft(x):
    return []

print(fft(list(map(int, input().split()))))
