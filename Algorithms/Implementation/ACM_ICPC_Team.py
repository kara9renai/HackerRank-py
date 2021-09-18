#!/bin/python3

import collections

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    stack = []
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            c = bin(int('0b'+topic[i], 0) | int('0b'+topic[j], 0))
            stack.append(c.count('1'))
    d = collections.Counter(stack)
    max_topics = 0
    max_counts = 0
    for key, val in d.items():
        if key > max_topics:
            max_topics = key
            max_counts = val
    return max_topics, max_counts
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print(result)