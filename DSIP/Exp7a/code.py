import cv2 as cv
import numpy as np


def negative(img, pix_max=255):
    return 255 - img


def disp_image(title, img, delay=3000):
    cv.imshow(title, img)
    cv.waitKey(delay)

def gray_slicing_with_bg(img, r1, r2, pix_max=255):
    img1 = img.copy()
    m, n = img1.shape
    for i in range(m):
        for j in range(n):
            img1[i][j] = 255 if r1 <= img1[i][j] <= r2 else img1[i][j]
    return img1


def gray_slicing_without_bg(img, r1, r2, pix_min=0, pix_max=255):
    img1 = gray_slicing_with_bg(img, r1, r2, pix_max)
    img1[img1 < r1] = pix_min
    img1[img1 > r2] = pix_min
    return img1


def threshold(img, theta, pix_min=0, pix_max=255):
    img1 = img.copy()
    img1[img1 < theta] = pix_min
    img1[img1 >= theta] = pix_max
    return img1


if __name__ == '__main__':
    img = cv.imread('img.png', 0)
    disp_image('og image', img)
    disp_image('gray slicing with bg', gray_slicing_with_bg(img, 100, 150))
    disp_image('gray slicing without bg', gray_slicing_with_bg(img, 100, 150))
    disp_image('negative image', negative(img))
    disp_image('thresholded image', threshold(img, 128))
