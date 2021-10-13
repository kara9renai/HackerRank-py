#!/bin/python3

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    if k == 0:
        return [ele for ele in range(1, n+1)]
    elif (n / k) % 2 != 0:
        return [-1]
    return [(i+1) + (1 if (i//k)%2==0 else -1) * k for i in range(n)]

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        print(' '.join(map(str, result)))