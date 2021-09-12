#!/bin/python3

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    bundle = []
    for p in keyboards:
        for q in drives:
            bundle.append(p+q)
    bundle.sort(reverse=True)
    for price in bundle:
        if b >= price:
            return price
    return -1

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)