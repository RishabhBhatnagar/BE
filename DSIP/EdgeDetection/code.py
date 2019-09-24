import cv2 as cv
import numpy as np


def get_g(z):
    gx = (-z[0] + z[2] - z[6] + z[8] + ((z[5] - z[3]) << 1))
    gy = (- z[0] - z[2] + z[6] + z[8] + ((z[7] - z[1]) << 1))
    return abs(gx + 1j * gy)


def applyFilter(_filter, img, pix_min=0, pix_max=255):
    m, n, = img.shape
    u, v = _filter.shape
    d1, d2 = m - u + 1, n - v + 1
    ans = np.zeros((d1, d2))

    for i in range(d1):
        for j in range(d2):
            z = img[i : i + u, j : j + v].flatten()
            ans[i][j] = get_g(z)
            input(ans[i, j])
    return ans


img = cv.imread('img.png', 0)
ans = applyFilter(np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]), img)
print(img.shape, ans.shape)
cv.imshow('end', ans)
cv.waitKey(2000)





'''
for 3d:
def applyFilter(_filter, img, pix_min=0, pix_max=255):
    m, n, _ = img.shape
    u, v = _filter.shape
    d1, d2 = m - u + 1, n - v + 1
    ans = np.zeros((d1, d2, 3))

    for i in range(d1):
        for j in range(d2):
            z = img[i : i + u, j : j + v].reshape(u * v, 3)
            zr = z[:, 0]
            zg = z[:, 1]
            zb = z[:, 2]
            ans[i][j] = tuple(map(get_g, [zr, zg, zb]))
    return ans
'''
