#!/bin/python3

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for idx, grade in enumerate(grades):
        if grade < 38:
            continue
        multiple = 0
        while grade > multiple:
            multiple += 5
        if (multiple - grade) < 3:
            grades[idx] = multiple
        else:
            continue
    return [c for c in grades]

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))