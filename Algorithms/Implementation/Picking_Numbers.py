#!/bin/python3

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    counts = []
    for i in range(len(a)):
        count = a.count(i)
        count += a.count(i+1)
        counts.append(count)
    return max(counts)

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))[:n]

    result = pickingNumbers(a)

    print(result)
