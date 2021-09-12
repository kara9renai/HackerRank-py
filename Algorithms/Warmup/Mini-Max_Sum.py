#!/bin/python3

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sums = []
    for _ in range(len(arr)):
        tail = arr[-1]
        arr.pop()
        sum = 0
        for j in arr:
            sum += j
        sums.append(sum)
        arr.insert(0, tail)
    min_sum = min(sums)
    max_sum = max(sums)
    print('{} {}'.format(min_sum, max_sum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
