#!/bin/python3

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    count = 0
    n_str = str(n)
    for ele in n_str:
        if int(ele) == 0:
            continue
        if n % int(ele) == 0:
            count += 1
    return count

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        print(result)