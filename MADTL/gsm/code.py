from functools import reduce


Fn = 1 << 22  # globally(publically) available frame number.



def split_n(num, n):
    ones = int('0b' + '1' * n, 2)
    lh = ones & num
    rh = (num - lh) >> n
    return lh, rh



def A3(rand, key):
    rand_l, rand_r = split_n(rand, 64)
    key_l, key_r = split_n(key, 64)
    l_xor = rand_l ^ key_r
    r_xor = rand_r ^ key_l

    final_xor = l_xor ^ r_xor
    res = reduce(int.__xor__, split_n(final_xor, 32))
    return res

 

if __name__ == '__main__':
    rand_no = 340282366920938463463374607431768211456
    key = 345282366920998463463374607431768211456
    print('Random Number:', rand_no)
    print('Key:', key)
    print('Output of A3 algorithm:', A3(rand_no, key))


'''
OUTPUT:
Random Number: 340282366920938463463374607431768211456
Key: 345282366920998463463374607431768211456
Output of A3 algorithm: 3492679906
'''

