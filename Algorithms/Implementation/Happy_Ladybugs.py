#!/bin/python3

def HappyLadybugs(b):
    count_dict = {}
    if b.count('_') == len(b):
        return 'YES'
    for letter in b:
        count_dict[letter] = b.count(letter)
    
    if any(count_dict[ele] == 1 for ele in count_dict if ele != "_"):
        return 'NO'
    else:
        if '_' in b:
            return 'YES'
        else:
            if b[0] != b[1]:
                return 'NO'
            else:
                for i in range(1, len(b)-1):
                    if b[i] != b[i+1] and b[i] != b[i-1]:
                        return 'NO'
                return 'YES'

if __name__ == "__main__":
    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())
        b = input()
        result = HappyLadybugs(b)
        print(result)