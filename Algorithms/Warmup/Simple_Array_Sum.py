#!/bin/python3

def simpleArraySum(ar):
    total = 0
    for ele in ar:
        total += ele
    return total

ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))[:ar_count]

result = simpleArraySum(ar)

print(result)