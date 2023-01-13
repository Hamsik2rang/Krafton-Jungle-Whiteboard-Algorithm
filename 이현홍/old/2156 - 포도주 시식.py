import sys

sys.stdin = open("input.txt", "r")

import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
memo = [[0] * (N) for _ in range(3)]
memo[0][0] = 0
memo[1][0] = arr[0]
memo[2][0] = arr[0]

for col in range(1, N):
    memo[0][col] = max(memo[i][col - 1] for i in range(3))
    memo[1][col] = memo[0][col - 1] + arr[col]
    memo[2][col] = max(memo[0][col - 1], memo[1][col - 1]) + arr[col]

print(max(memo[i][N - 1] for i in range(3)))
