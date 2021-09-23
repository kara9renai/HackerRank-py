#!/bin/python3

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    stack = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                stack.append(abs(i - j))
    if stack:
        return min(stack)
    else:
        return -1

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)