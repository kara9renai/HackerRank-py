#!/bin/python3
import math


def jumpingOnClouds(c, k):
    e = 100
    if len(c) % k != 0:
        gcd = math.gcd(len(c), k)
        if gcd == 1:
            c = c * k
        else:
            c = c * gcd
    for idx in range(0, len(c), k):
        if c[idx] == 1:
            e -= 3
        else:
            e -= 1
    return e

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)
