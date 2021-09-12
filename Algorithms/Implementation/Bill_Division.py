#!/bin/python3

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bills, k, charged):
    total = 0
    bills.remove(bills[k])
    for bill in bills:
        total += bill
    actual = total // 2
    d = charged - actual
    if d > 0:
        print(d)
    elif d == 0:
        print('Bon Appetit')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
