#!/bin/python3

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, arr):
    count = 0
    reminder = [0] * k
    for i in range(len(arr)):
        reminder[arr[i]%k] += 1
    for i in range(1, k):
        if i < k - i:
            # i + k - i = k
            # the sum of 2values (reminder[i],  reminder[k-i]) is divisible by k
            count += max(reminder[i], reminder[k-i])
    if (k % 2 == 0) and (reminder[k // 2] > 0):
        count += 1
    if reminder[0] != 0:
        count += 1
    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)