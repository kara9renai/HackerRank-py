#!/bin/python3

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    count = 0
    i = 0
    while i + m <= len(s):
        sub_string = s[i:i+m]
        total = 0
        for j in sub_string:
            total += j
        if d == total:
            count += 1
        i += 1
    return count
    

if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)
