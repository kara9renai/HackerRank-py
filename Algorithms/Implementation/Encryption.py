#!/bin/python3

import math
from itertools import zip_longest

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    arr = []
    brr = []
    row = int(math.sqrt(len(s)))
    if row ** 2 == len(s):
        column = row
    else:
        column = row + 1
    for i in range(0, len(s), column):
        arr.append(s[i:i+column])
    for ele in zip_longest(*arr, fillvalue=' '):
        word = ''
        for e in ele:
            word += e
        brr.append(word.rstrip())
    return ' '.join(brr)
    

if __name__ == '__main__':
    s = input()

    result = encryption(s)

    print(result)