import sys
sys.stdin=open("input.txt", "r")
input=sys.stdin.readline


n=int(input())
dp=[[0]*n for _ in range(2)]

for idx in range(n):
    dp[0][idx]=int(input())

if n>2:
    dp[1][0]=dp[0][0]
    dp[1][1]=dp[0][0]+dp[0][1]
    dp[1][2]=max(dp[1][1], dp[0][0]+dp[0][2], dp[0][1]+dp[0][2])
    for i in range(3,n):
        dp[1][i]=max(dp[1][i-1], dp[0][i]+dp[1][i-2], dp[0][i]+dp[0][i-1]+dp[1][i-3])

    print(max(dp[1]))
else:
    print(sum(dp[0]))