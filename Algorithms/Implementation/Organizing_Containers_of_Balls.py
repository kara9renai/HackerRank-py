#!/bin/python3

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    columns = [sum(i) for i in container]
    rows = [sum(i) for i in zip(*container)]
    if sorted(columns) == sorted(rows):
        return "Possible"
    else:
        return  "Impossible"

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)