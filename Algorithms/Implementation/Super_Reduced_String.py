#!/bin/python3

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def create(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            return s

def isTrue(s):
    return any(s[i] == s[i+1] for i in range(len(s)-1))

def superReducedString(s):
    if isTrue(s):
        s = create(s)
        return superReducedString(s)
    else:
        return s if s else 'Empty String'

if __name__ == '__main__':
    s = input()

    result = superReducedString(s)

    print(result)