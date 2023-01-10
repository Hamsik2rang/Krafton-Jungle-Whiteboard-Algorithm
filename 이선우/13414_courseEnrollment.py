import sys

sys.stdin = open("input.txt", "r")

import sys

limit, count = map(int, sys.stdin.readline().split())
student_list = {}
i = 1

for _ in range(count):
    new = str(sys.stdin.readline().rstrip())
    student_list[new] = i
    i += 1

student_list = sorted(student_list, key = lambda i : student_list[i])
if len(student_list) < limit:
    limit = len(student_list)

for ans in range(limit):
    print(student_list[ans])