class FuzzyElement:
    def __init__(self, val, mu):
        self._mu = mu
        self.val = val
        self._tup = (self.val, self.mu)
    def __iter__(self):
        return self._tup.__iter__()
    @property
    def mu(self):
        return self._mu
    def __repr__(self):
        return self._tup.__repr__()


class FuzzySet(dict):

    def __init__(self, elements):
        # elements should be non-lazy iterable of pairs (C, μ)
        # μ: membership operator value 
        # 0 \le μ \le 1
        # C: value of the element in crisp set.

        if self.check_format(elements):
            super().__init__(map(lambda x: FuzzyElement(*x), elements))
        else:
            raise TypeError("Invalid input for fuzzy sets.")
    def intersection():
        pass
        
    def check_format(self, elements):
        return all((len(pair) == 2) and (0 <= pair[1] <= 1) for pair in elements)


a = FuzzySet([(1, .2), (1, .2), (1, .2)])

