#!/bin/python3

def diagonalDifference(arr):
    primary = 0
    secondary = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                primary += arr[i][j]
            if i + j == len(arr)-1:
                secondary += arr[i][j]
    diff = abs(primary - secondary)
    return diff

def main():
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)

if __name__ == '__main__':
    main()