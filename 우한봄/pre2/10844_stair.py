#문제 시간 제한: 1초
#문제의 최대 N값: 자리수 100
#허용되는 최대 시간복잡도: 10*n
#알고리즘: dp
# 1자리:0제외, 1~8 뒤에 올 수 있는 수는 2종료, 9뒤엔 8만 올 수 있음
# 0 : dp[자리수][0]=dp[자리수-1][1]
# 1~8: dp[자리수][n]=dp[자리수-1][n-1]+dp[자리수-1][n+1]
# 9: dp[자리수][9]=dp[자리수-1][8]

import sys
input=sys.stdin.readline

REM=1_000_000_000

n=int(input())
# dp=[[0]*10]*(n+1)
dp = [[0]*10 for _ in range(n+1)]
for i in range(1,10):
    dp[1][i]=1

print(dp)
# print(dp2)
for nd in range(2,n+1):
    for i in range(10):
        if i==0:
            dp[nd][i]=dp[nd-1][1]
        elif i==9:
            dp[nd][i]=dp[nd-1][8]
        else:
            dp[nd][i]=dp[nd-1][i-1]+dp[nd-1][i+1]

print(sum(dp[n])%REM)