#!/bin/python3

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    specialChar = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
    constraints_dict = {
        "lower": False,
        "upper": False,
        "digit": False,
        "special": False
    }
    for ele in password:
        if ele.isupper():
            constraints_dict["upper"] = True
        elif ele.islower():
            constraints_dict["lower"] = True
        elif ele.isdigit():
            constraints_dict["digit"] = True
        elif ele in specialChar:
            constraints_dict["special"] = True
    
    count = 0
    for flag in constraints_dict.values():
        if flag == False:
            count += 1
    
    if n >= 6:
        return count
    
    else:
        if n + count < 6:
            return 6 - n
        else:
            return count
               

if __name__ == '__main__':
    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)
    
    print(str(answer))