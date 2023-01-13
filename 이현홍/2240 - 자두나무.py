import sys

sys.stdin = open("input.txt", "r")

import sys

T, W = map(int, sys.stdin.readline().split())
location = 1
drops = list(map(int, sys.stdin.readlines()))
memo = [[0] * T for _ in range(W + 1)]
if drops[0] == 1:
    memo[0][0] += 1
else:
    memo[1][0] += 1

for col in range(1, T):
    for row in range(W + 1):
        n = 2 if row % 2 else 1
        add = 1 if n == drops[col] else 0
        if row == 0:
            memo[row][col] = memo[row][col - 1] + add
        else:
            memo[row][col] = max(memo[row - 1][col - 1], memo[row][col - 1]) + add

print(max(memo[row][T - 1] for row in range(W + 1)))
