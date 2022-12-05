import sys

sys.stdin = open("input.txt", "r")

import sys

iter = int(sys.stdin.readline())
dp = [0 for _ in range(iter)]
task_list = []

for _ in range(0, iter):
    task_list.append(list(map(int, sys.stdin.readline().split())))

for days in range(1, iter + 1):
    for task in range(0, days):
        if task_list[task][0] > days:
            pass
        

print(task_list)