import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
memo = [[0 for _ in range(2)] for _ in range(n)]

answer = memo[0][0] = memo[0][1] = seq[0]

for i in range(1, n):
    pass
    memo[i][0] = max(memo[i - 1][0] + seq[i], seq[i])
    memo[i][1] = max(memo[i - 1][1] + seq[i], memo[i - 1][0])
    answer = max(answer, memo[i][0], memo[i][1])

print(answer)
