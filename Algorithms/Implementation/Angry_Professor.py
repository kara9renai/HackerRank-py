#!/bin/python3

def angryProfessor(threhold, arrival_times_list):
    attendance_num = 0
    for arrival_times in arrival_times_list:
        if arrival_times <= 0:
            attendance_num += 1
    if attendance_num >= threhold:
        print('NO')
    else:
        print('YES')

t = int(input().strip())

for i_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])
    
    a = list(map(int, input().rstrip().split()))

    angryProfessor(k, a)
