import sys
inf = sys.maxsize
input = sys.stdin.readline

n = int(input())
r = list(input().rstrip())
dp = [inf for _ in range(n)]

dp[0] = 0
for i in range(1, n):
    for j in range(i):
        if (r[j] == "B" and r[i] == "O") or (r[j] == "O" and r[i] == "J") or (r[j] == "J" and r[i] == "B"):
            dp[i] = min(dp[i], dp[j] + (i-j)**2)
print(dp[n-1] if dp[n-1] != inf else -1)
