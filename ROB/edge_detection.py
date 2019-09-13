def mag_del_i(k, j, I, del_x, del_y):
    i1 = (abs(I[k + 1][j] - I[k][j]) + abs(I[k + 1][j + 1] - I[k][j + 1])) / del_x
    i2 = (abs(I[k][j + 1] - I[k][j]) + abs(I[k + 1][j + 1] - I[k + 1][j])) / del_y
    i1 /= 2
    i2 /= 2
    return abs(i1 + 1j * i2)


def algo(img, del_x, del_y):
    m = len(img)
    n = len(img[0])
    k = j = 0
    epsilon = 2
    dp = [[0 for j in range(n)] for i in range(m)]
    for k in range(m - 1):
        for j in range(n - 1):
            if mag_del_i(k, j, img, del_x, del_y) >= epsilon:
                dp[k][j] = 1
    return dp

if __name__ == '__main__':
    img_intensities = [
        [0, 0, 5, 0],
        [0, 0, 4, 0],
        [0, 0, 3, 0],
        [0, 0, 4, 0],
        [0, 0, 0, 0]
    ]
    print(*algo(img_intensities, 1, 1), sep="\n")
