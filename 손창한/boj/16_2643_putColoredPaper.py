import sys
input = sys.stdin.readline

n = int(input())
ppr = sorted(list(sorted(list(map(int, input().split()))) for _ in range(n)))
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if ppr[i][1] >= ppr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
