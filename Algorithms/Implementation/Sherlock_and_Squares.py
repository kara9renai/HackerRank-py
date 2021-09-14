#!/bin/python3

import math

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    count = 0
    while a <= b:
        x = int(math.sqrt(a))
        if a == x ** 2:
            count += 1
            a += 2 * x + 1
        else:
            a += 1
    return count

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        print(result)