import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    fl = list(map(int, input().split()))
    dp = [[0 for _ in range(k+1)] for _ in range(k+1)]
    # set dp
    for i in range(k-1):
        dp[i][i+1] = fl[i] + fl[i+1]
        for j in range(i+2, k):
            dp[i][j] = dp[i][j-1] + fl[j]
    # div
    for p in range(2, k):
        # conq
        for i in range(k-p):
            j = i + p
            dp[i][j] += min([dp[i][k] + dp[k+1][j] for k in range(i, j)])
    print(dp[0][k-1])