#!/bin/python3

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    hours_dict = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve'
    }

    minutes_dict = {
        0: "o' clock", 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
        23: 'twenty three', 24: 'twenty four', 25: 'twenty five',
        26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight',
        29: 'twenty nine', 30: 'half'
    }

    if m == 0:
        return hours_dict[h] + " " + minutes_dict[m]
    elif m == 1:
        return minutes_dict[m] + " minute past " + hours_dict[h]
    elif 1 < m < 15 or 15 < m < 30:
        return minutes_dict[m] + " minutes past " + hours_dict[h]
    elif m == 15 or m == 30:
        return minutes_dict[m] + " past " + hours_dict[h]
    elif m > 30 and 60 - m > 1:
        if 60 - m != 15:
            return minutes_dict[60-m] + " minutes to " + hours_dict[h+1]
        else:
            return minutes_dict[60-m] + ' to ' + hours_dict[h+1]
    elif m > 30 and 60 - m == 1:
        return minutes_dict[60-m] + " minute to " + hours_dict[h+1]

if __name__ == '__main__':
    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    print(result)