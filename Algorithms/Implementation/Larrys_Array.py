#!/bin/python3

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    count = 0
    for i in range(1, len(A)):
        for j in range(i):
            if A[i] < A[j]:
                count += 1
    return 'YES' if count % 2 == 0 else 'NO'

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        print(result)