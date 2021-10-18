#!/bin/python3

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    while any(s[i] == s[i+1] for i in range(len(s)-1)):
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s.replace(s[i]+s[i+1], "")
                break 
    if len(s) == 0:
        return 'Empty String'
    return s

if __name__ == '__main__':
    s = input()

    result = superReducedString(s)

    print(result)