#!/bin/python3

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    count = 0
    for ele in s:
        if ele.isupper():
            count += 1
    return count + 1

if __name__ == '__main__':
    s = input()

    result = camelcase(s)
    
    print(str(result))