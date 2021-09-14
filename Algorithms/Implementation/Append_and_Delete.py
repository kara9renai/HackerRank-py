#!/bin/python3

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

# This problem was difficult for me to solve. So I tried making answers to this problem 
# while referencing discussions.

def appendAndDelete(s, t, k):
    ls = len(s)
    lt = len(t)
    q = 0
    if ls + lt <= k:
        return 'Yes'
        # There are more operations than the combined length.
        # You can peform as many deletions as needed on an empty string.
    for i in range(min(ls, lt)):
        if s[i] == t[i]:
            q = i
        else:
            break
    q = (ls-q-1) + (lt-q-1)
    # the number of operations required to make the strings equal
    if q <= k and (k - q) % 2 == 0:
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result)