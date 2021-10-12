#!/bin/python3

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    total = 0
    
    total += H * W * 2
    
    def check(itr):
        t = 0
        for idx in  range(len(itr)-1):
            t += abs(itr[idx+1]-itr[idx])
        return t
    
    def first_and_end(itr):
        return itr[0] + itr[-1]
    
    for a in A:
        total += check(a)
        total += first_and_end(a)
    
    for a in zip(*A):
        total += check(a)
    
    total += sum(A[0])
    total += sum(A[-1])
    
    return total

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print(result)