#!/bin/python3

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    distance_1 = abs(x - z)
    distance_2 = abs(y - z)
    if distance_1 < distance_2:
        return 'Cat A'
    elif distance_2 < distance_1:
        return 'Cat B'
    else:
        return 'Mouse C'
    
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)