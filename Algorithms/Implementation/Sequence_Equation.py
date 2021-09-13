#!/bin/python3

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    for i in range(1, len(p)+1):
        q = p.index(i) + 1
        print(p.index(q) + 1)

n = int(input().strip())

p = list(map(int, input().rstrip().split()))

permutationEquation(p)
