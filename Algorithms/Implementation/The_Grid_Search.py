#!/bin/python3

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    count = 0
    for i in range(len(G[0]) - len(P[0])+1):
        for j in range(len(G)-len(P)+1):
            if G[j][i:i+len(P[0])] == P[0]:
                for x in range(1, len(P)):
                    if G[j+x][i:i+len(P[0])] == P[x]:
                        count += 1
                        if count == len(P) - 1:
                            return 'YES'
    return 'NO'

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result)