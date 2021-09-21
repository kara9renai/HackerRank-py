#!/bin/python3


#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    count = 0
    def splitAndSum(n):
        s = str(n)
        if len(s) == 1:
            arr = list(map(int, s))
            return sum(arr)
        else:
            sl = s[:len(s) // 2]
            sr = s[len(s) // 2:]
            return int(sl) + int(sr)
    
    for ele in range(p, q+1):
        m = splitAndSum(ele ** 2)
        if ele == m:
            print(ele, end=" ")
            count += 1
    
    if count == 0:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
