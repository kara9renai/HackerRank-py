#!/bin/python3

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    p_ratio = positive / len(arr)
    n_ratio = negative / len(arr)
    z_ratio = zero / len(arr)
    return '{:.6f}\n{:.6f}\n{:.6f}'.format(p_ratio, n_ratio, z_ratio)

if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)

    print(result)