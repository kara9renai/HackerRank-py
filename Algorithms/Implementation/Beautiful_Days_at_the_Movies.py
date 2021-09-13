#!/bin/python3

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    count = 0
    for num in range(i, j+1):
        reversed_num = int(str(num)[::-1])
        if abs(num - reversed_num) % k == 0:
            count += 1
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    print(result)
