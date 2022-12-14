import sys

sys.stdin = open("input.txt", "r")

import sys

def solve(total, idx):
    global ans_min, ans_max

    if idx == (iter - 1):
        ans_min = min(ans_min, total)
        ans_max = max(ans_max, total)
        return

    for i in range(4):
        if operator_list[i] != 0:
            operator_list[i] -= 1
            if i == 0:
                solve(total + num_list[idx + 1], idx + 1)
            elif i == 1:
                solve(total - num_list[idx + 1], idx + 1)
            elif i == 2:
                solve(total * num_list[idx + 1], idx + 1)
            else:
                solve(int(total / num_list[idx + 1]), idx + 1)

            operator_list[i] += 1

iter = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
operator_list = list(map(int, sys.stdin.readline().split()))
ans_max = -1000000000
ans_min = 1000000000

solve(num_list[0], 0)
print(ans_max)
print(ans_min)