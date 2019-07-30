linear_conv = lambda s1, s2: (lambda a, n1, n2: [sum([a[i * n2 + j] for i in range(n1) for j in range(n2) if i + j == s and i < n1 and j < n2]) for s in range(n1 + n2 - 1)])(*(lambda sn1, sn2:(list(__import__('itertools').starmap(__import__('operator').mul, __import__('itertools').product(sn1[0], sn2[0]))), sn1[1], sn2[1]))(*(lambda x, h: [*map(lambda x: (x, len(x)), [x, h])])(s1, s2))
)

from itertools import islice, cycle

circular_conv = lambda x, h: list(islice((lambda gen, div: (gen, islice(gen, div)))(cycle(x[::-1]), 5)[0], 4))
print(circular_conv([1, 2, 3, 4], [2, 4, 5]))
