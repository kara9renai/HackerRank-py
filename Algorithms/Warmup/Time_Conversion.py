#!/bin/python3

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hh = int(s[0])
    ampm = s[-1][2:]
    if ampm == "AM":
        if hh == 12:
            s[0] = '00'
    elif ampm == "PM":
        if hh != 12:
            hh += 12
            s[0] = str(hh)
    string = '{}:{}:{}'.format(s[0], s[1], s[2][:2])
    return string
     
if __name__ == '__main__':
    s = input().split(":")

    result = timeConversion(s)

    print(result)