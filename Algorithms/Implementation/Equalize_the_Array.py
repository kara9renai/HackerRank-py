#!/bin/python3

from collections import Counter as c

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    count = 0
    m = list(c(arr).values())
    m.sort()
    for i in range(len(m)-1):
        count += m[i]
    return count
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)