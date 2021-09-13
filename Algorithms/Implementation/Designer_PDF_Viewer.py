#!/bin/python3
import string


def designerPdfViewer(high_list, word):
    strings = string.ascii_lowercase
    d = {alphabet: height for alphabet, height in zip(strings, high_list)}
    h_stack = []
    for letter in word:
        if letter in d:
           h_stack.append(d[letter])
    return len(word) * max(h_stack) 

h = list(map(int, input().rstrip().split()))
word = input()
result = designerPdfViewer(h, word)
print(result)
