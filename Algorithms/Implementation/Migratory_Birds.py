#!/bin/python3

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    bird_type = 1
    l = arr.count(1)
    for i in range(2, 6):
        m = arr.count(i)
        if l < m:
            l = m
            bird_type = i
    return bird_type

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)