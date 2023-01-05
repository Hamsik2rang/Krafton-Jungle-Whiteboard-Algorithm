import sys

sys.stdin = open("input.txt", "r")

import sys

N = int(sys.stdin.readline())
arr = [[0] * N for _ in range(10)]

for r in range(1, 10):
    arr[r][0] = 1

for c in range(N - 1):
    for r in range(10):
        if 0 <= r - 1:
            arr[r - 1][c + 1] += arr[r][c]
        if r + 1 <= 9:
            arr[r + 1][c + 1] += arr[r][c]


result = 0
for r in range(10):
    result += arr[r][N - 1]

print(result)
