#!/bin/python3

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(string, n):
    return string.count('a') * (n // len(string)) + string[:n%len(string)].count('a')   

if __name__ == '__main__':
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)