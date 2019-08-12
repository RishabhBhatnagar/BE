import math
from math import sin, cos

dft = lambda x, N: [
                    (lambda c: round(c.real, 3) + 1j * round(c.imag, 3))
                     (
                      (lambda k: \
                         sum(
                            x[n] \
                            * (cos(2 * math.pi * n * k / N) \
                            - 1j
                            * sin(2 * math.pi * n * k / N)) \
                            for n in range(N))
                      )(i)
                    ) for i in range(N)
                ]


ip = [0, 1, 2, 3]
N = 4

print("Input Sequence:", ip)
print("Performing DFT using {} points".format(N))
print("DFT sequence:", dft(ip, N))
