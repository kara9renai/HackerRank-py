#!/bin/python3

def staircase(n):
    char = "#"
    for i in range(1, n+1):
        print(" " * (n - i) + char * i)

n = int(input().strip())
staircase(n)