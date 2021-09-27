#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    d = max(c[0], n - 1 - c[-1])
    for i in range(len(c) - 1):
        d = max((c[i+1] - c[i]) // 2, d)
    return d
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)