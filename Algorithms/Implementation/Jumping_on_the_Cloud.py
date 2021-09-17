#!/bin/python3

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    m = 0
    path = len(c) - 1
    for idx, ele in enumerate(c):
        if ele == 1:
            path -= 1
            m = idx + 1
        if idx - m == 2:
            path -= 1
            m = idx
    return path

if __name__ == '__main__':
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)