import sys
input=sys.stdin.readline

n=int(input())
int_lst=list(map(int,input().split()))
dp=[[0] * n for _ in range(2)]

# print(int_lst)
dp[0][0]=int_lst[0]

if max(int_lst)<0:
    rst=max(int_lst)
else:
    if n>1:

        rst=0
        for idx in range(1,len(int_lst)):
            dp[0][idx]=max(int_lst[idx]+dp[0][idx-1], int_lst[idx])
            dp[1][idx]=max(int_lst[idx]+dp[1][idx-1],dp[0][idx-1])
            
            # print(dp)
            rst=max(rst, dp[0][idx], dp[1][idx])

    else: rst=dp[0][0]

print(rst)