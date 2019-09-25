import cv2 as cv
import numpy as np


HSOBEL_WEIGHTS = np.array([[1, 2, 1],
                           [0, 0, 0],
                           [-1, -2, -1]]) / 4.0
VSOBEL_WEIGHTS = HSOBEL_WEIGHTS.T


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


img = cv.imread('img.png', 0)
ans = sobel(img)
cv.imshow('end', ans)
cv.waitKey(3000)
