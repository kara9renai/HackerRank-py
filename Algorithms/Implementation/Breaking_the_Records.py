#!/bin/python3

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    high_count = 0
    low_count = 0
    high_idx = 0
    low_idx = 0
    idx = 0
    while idx < len(scores):
        if scores[high_idx] < scores[idx]:
            high_idx = idx
            high_count += 1
        elif scores[low_idx] > scores[idx]:
            low_idx = idx
            low_count += 1
        idx += 1
    return high_count, low_count

if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)