import sys

n = int(sys.stdin.readline())
wine = [0] * n
for i in range(n):
    wine[i] = int(sys.stdin.readline())

memo = [-1 for _ in range(n)]

memo[0] = wine[0]

if n > 1:
    memo[1] = wine[0] + wine[1]

if n > 2:
    memo[2] = max(wine[2] + wine[1], wine[2] + wine[0], wine[1] + wine[0])

for i in range(3, n):
    memo[i] = max(
        memo[i - 3] + wine[i - 1] + wine[i], wine[i] + memo[i - 2], memo[i - 1]
    )

print(memo[n - 1])
