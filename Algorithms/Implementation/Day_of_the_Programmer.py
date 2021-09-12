#!/bin/python3

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    elif (year % 4 == 0) and ((year < 1918) or (year % 400 == 0) or (year % 100 != 0)):
        return '12.09.{}'.format(str(year))
    else:
        return '13.09.{}'.format(str(year))
    
if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)