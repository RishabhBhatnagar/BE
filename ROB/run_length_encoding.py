def algo(arr):
    count = 1
    prev = arr[0]
    ans = []
    for ele in arr[1:]:
        if ele == prev:
            count += 1
        else:
            ans.extend((prev, count))
            count  = 1
        prev = ele
    else:
        ans.extend((prev, count))
    return ans


if __name__ == '__main__':
    ip = tuple(map(int, input('enter the ip sequence(without spaces): ')))
    op = algo(ip)

    print('output sequence:', op)
    print('original space requirement:', len(ip) * 8)
    print('space requirement of output:', len(op) * 8)
