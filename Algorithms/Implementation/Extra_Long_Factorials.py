#!/bin/python3

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    factorial = 1
    for num in range(1, n+1):
        factorial *= num
    print(factorial)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
