import sys
input = sys.stdin.readline

n = int(input())
dp = list(range(n+1))

for i in range(7, n+1):
            # 234 4: 2n, 234 44: 3n, 234 444: 4n
    dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
print(dp[n])
