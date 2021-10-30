#!/bin/python3

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    stored_val = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > stored_val:
            arr[i+1] = arr[i]
            print(' '.join(map(str, arr)))
            if not i:
                arr[i] = stored_val
                print(' '.join(map(str, arr)))
        else:
            arr[i+1] = stored_val
            print(' '.join(map(str, arr)))
            break
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
