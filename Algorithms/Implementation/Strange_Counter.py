#!/bin/python3

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    time = 1
    value = 3
    while time < t:
        time += value
        value *= 2
    if t == time:
        return value - (t-time)
    else:
        return value // 2 - (t - (time - (value // 2)))

if __name__ == '__main__':
    t = int(input().strip())

    result = strangeCounter(t)

    print(result)