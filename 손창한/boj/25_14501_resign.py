import sys
input = sys.stdin.readline

n = int(input())
a = list(list(map(int, input().split())) for _ in range(n))
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    t, p = a[i]
    if i + t <= n:
        dp[i] = max(dp[i+1], dp[i+t]+p)
    else:
        dp[i] = dp[i + 1]
print(dp[0])
