import sys
input = sys.stdin.readline

n = int(input())
# dp[value][place]
dp = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        if j == 0: # only up
            dp[i][j] = dp[i-1][1]
        elif j == 9: # only down
            dp[i][j] = dp[i-1][8]
        else: # up + down
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 10**9)