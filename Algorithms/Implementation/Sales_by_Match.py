#!/bin/python3

import collections

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pairs = 0
    ar = ar[:n]
    d = collections.Counter(ar)
    for e in d.values():
        f = e // 2
        pairs += f
    return pairs
    

if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)