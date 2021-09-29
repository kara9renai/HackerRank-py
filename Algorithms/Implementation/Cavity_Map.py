#!/bin/python3

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    if len(grid) == 1:
        return grid
    stack = []
    stack.append(grid[0])
    for i in range(1, len(grid)-1):
        tmp = list(grid[i])
        for j in range(1, len(grid)-1):
            ele = int(tmp[j])
            if ele > int(grid[i-1][j:j+1]) \
            and ele > int(grid[i][j-1:j]) \
            and ele > int(grid[i][j+1:j+2]) \
            and ele > int(grid[i+1][j:j+1]):
                tmp[j] = 'X'
        stack.append(''.join(tmp))
    stack.append(grid[-1])
    return stack

if __name__ == '__main__':
    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print(''.join(result))