#!/bin/python3

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    pages = min(p//2,n//2-p//2)
    return pages

if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())
    
    result = pageCount(n, p)

    print(result)