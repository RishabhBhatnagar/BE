from math import sin, cos
from matplotlib import pyplot as plt


signal = lambda t: ((t + 1) ** 0.2 + t **2 *  (cos(2 * t)))


def sample_signal(signal, n_samples, time_period=1):
    # signal's last parameter must be time.
    return [signal(t * time_period) for t in range(n_samples)]


def plot_signal(samples, discrete=True, title="Sample"):
    plt.title(title)
    n = len(samples)
    if discrete:
        plt.stem(range(n), samples)
    else:
        plt.plot(samples)
        plt.axhline(y=0, color='red')
    plt.show()


if __name__ == '__main__':
    samples = sample_signal(signal, 120, time_period=0.1)
    plot_signal(samples, discrete=True, title="Discrete Signal")
    plot_signal(samples, discrete=False, title="Reconstructed Signal")

