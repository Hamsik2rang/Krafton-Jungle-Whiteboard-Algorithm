import sys
input = sys.stdin.readline
n = int(input())
dp = [i for i in range(0, n+1)]

for i in range(7, n + 1):
    for j in range(3, n + 1):
        if i - j < 0:
            break
        dp[i] = max((j - 1) * dp[i - j], dp[i])

print(dp[n])