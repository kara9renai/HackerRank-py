#!/bin/python3

import collections

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    arr.sort()
    c = collections.Counter(arr)
    c.pop(max(arr))
    sticks_cut = len(arr)
    print(sticks_cut)
    for i in c.values():
        sticks_cut -= i
        print(sticks_cut)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))[:n]

    result = cutTheSticks(arr)
