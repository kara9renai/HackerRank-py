#!/bin/python3

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    count = 0
    l = [i for i, ele in enumerate(B) if ele % 2 == 1]
    if len(l) % 2 == 1:
        return 'NO'
    else:
        for i in range(0, len(l), 2):
            count += (l[i+1] - l[i]) * 2
        return str(count)

if __name__ == '__main__':
    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(result)