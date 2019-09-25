import cv2 as cv
import numpy as np


HSOBEL_WEIGHTS = np.array([[1, 2, 1],
                           [0, 0, 0],
                           [-1, -2, -1]]) / 4.0
VSOBEL_WEIGHTS = HSOBEL_WEIGHTS.T

HPREWITT_WEIGHTS = np.array([[1, 1, 1],
                             [0, 0, 0],
                             [-1, -1, -1]]) / 4.0
VPREWITT_WEIGHTS = HSOBEL_WEIGHTS.T


def convolve(img, mask):
    m, n, = img.shape
    u, v = mask.shape
    d1, d2 = m - u + 1, n - v + 1
    ans = np.zeros((d1, d2))
    for i in range(d1):
        for j in range(d2):
            ans[i][j] = sum((img[i : i + u, j : j + v] * mask).flatten())
    return ans


def sobel(img):
    img = img / 255         # normalising 
    sobel_h = convolve(img, HSOBEL_WEIGHTS)
    sobel_v = convolve(img, VSOBEL_WEIGHTS)
    return abs(sobel_h + 1j * sobel_v)

def prewitt(img):
    img = img / 255         # normalizing 
    prewitt_h = convolve(img, HPREWITT_WEIGHTS)
    prewitt_v = convolve(img, VPREWITT_WEIGHTS)
    return abs(prewitt_h + 1j * prewitt_v)


if __name__ == '__main__':
    img = cv.imread('img.png', 0)
    cv.imshow('sobel', sobel(img))
    cv.waitKey(3000)
    cv.imshow('prewitt', prewitt(img))
    cv.waitKey(3000)


