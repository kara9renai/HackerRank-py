#!/bin/python3

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    height = 0
    valleys_count = 0
    path = path[:steps]
    for step in path:
        if step == 'U':
            height += 1
        elif step == 'D':
            height -= 1
        if height == 0 and step == 'U':
            valleys_count += 1
    return valleys_count

if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)