import sys

sys.stdin = open("input.txt", "r")

import sys

iter = int(sys.stdin.readline())
dp = [0 for _ in range(iter)]
prerequisite_list = [[] for _ in range(iter)]

for i in range(0, iter):
    task = list(map(int, input().split()))
    dp[i] = task[0]

    if task[1] == 0:
        continue

    for prerequisite in task[2:]:
        prerequisite_list[i].append(prerequisite)

for i in range(0, iter):
    time = 0
    for j in prerequisite_list[i]:
        time = max(time, dp[j - 1])
    dp[i] += time
    
print(max(dp))