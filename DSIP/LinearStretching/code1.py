from collections import Counter
from matplotlib import pyplot as plt


class Histogram:
    def __init__(self, img: list):
        self.img = img
        self.n = len(img)
        self._hist = Counter(img)
        self.elements = self._hist.keys()
        self.freq = self._hist.values()
    
    def linear_stretching(self, smin, smax):
        rmax = max(self.elements)
        rmin = min(self.elements)
        m = (smax - smin) / (rmax - rmin)
        ans = []
        for r, f in self._hist.items():
            ans.extend([m * (r - rmin) + smin] * f)
        return Histogram(ans)
    
    def __repr__(self):
        return self._hist.__repr__()
    
    def plot(self, title=None, show=True, marker='-'):
        if title is not None:
            plt.title(title)
        plt.stem(self.elements, self.freq, linefmt=marker)
        if show:
            plt.show()


if __name__ == '__main__':
    ip = [2] * 50 + [3] * 60 + [4] * 50 + [5] * 20 + [6] * 10
    hist = Histogram(ip)
    stretched_hist = hist.linear_stretching(0, 7)
    
    plt.xlim([-2, 10])
    hist.plot("Initial Histogram")
    plt.xlim([-2, 10])
    stretched_hist.plot("Stretched Histogram")

