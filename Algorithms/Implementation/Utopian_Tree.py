#!/bin/python3

def utopiaTree(n):
    height = 1
    for period in range(1, n+1):
        if period % 2 == 0:
            height += 1
        else:
            height *= 2
    print(height)

t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    utopiaTree(n)
