#!/bin/python3

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    maxSum = [x for x in arr[1:]]
    minSum = [x for x in arr[:len(arr)-1]]
    print(sum(minSum), sum(maxSum))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
