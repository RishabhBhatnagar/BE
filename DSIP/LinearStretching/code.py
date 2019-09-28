import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_histogram(img, title=None):
    histogram = cv.calcHist([img], [0], None, [256], [0, 256])
    if title is not None:
        plt.title(title)
    plt.plot(range(len(histogram)), histogram)
    plt.show()


def linear_stretching(img1, s1, s2):
    img = img1.copy()
    flat = img.flatten()
    r1 = min(flat)
    r2 = max(flat)
    return (((s2 - s1) / (r2 - r1)) * (img - r1) + s1).astype(np.uint8)


if __name__ == '__main__':
    img = cv.imread('img.jpg', 0)
    stretched = linear_stretching(img, 0, 255)
    cv.imshow('original image', img)
    cv.imshow('stretched image', stretched)
    cv.waitKey(15000)
    plot_histogram(img, title='original image\'s histogram')
    plot_histogram(stretched, title='stretched image\'s histogram')

