#!/bin/python3

def viralAdvertising(n):
    total = 0
    ppl = 5
    for day in range(1, n+1):
        likes_ads = ppl // 2
        total += likes_ads
        ppl = likes_ads * 3
    print(total)

n = int(input().strip())

viralAdvertising(n)
