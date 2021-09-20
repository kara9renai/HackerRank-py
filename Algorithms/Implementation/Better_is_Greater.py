#!/bin/python3

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    arr = []
    for ele in w:
        arr.append(ord(ele))
    
    i = len(w) - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i <= 0:
        return 'no answer'
    
    j = len(w) - 1
    while arr[j] <= arr[i-1]:
        j -= 1
    arr[j], arr[i-1] = arr[i-1], arr[j]
    arr[i:] = arr[len(arr):i-1:-1]
    word = ''
    for letter in arr:
        word += chr(letter)
    return word

if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)