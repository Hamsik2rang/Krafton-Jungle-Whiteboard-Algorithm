import sys
input = sys.stdin.readline

N = int(input())

workArr = [[0, 0]]
for n in range(1, N + 1) :
    workArr.append(list(map(int, input().split())))
    
# print(workArr)
# print(MAXVAL)

dp = [[0 for i in range(N + 1)] for j in range(N + 1)]

for workNum in range(1, N + 1) :
    start = workNum
    howLong = workArr[workNum][0]
    value = workArr[workNum][1]
    
    for workDay in range(1, N + 1) : 
        if (start + howLong - 1 == workDay) : 
            dp[workNum][workDay] = max(dp[workNum - 1][workDay], value + dp[workNum - 1][workDay - howLong]) 
        else : 
            dp[workNum][workDay] = max(dp[workNum][workDay - 1], dp[workNum - 1][workDay])       
print(dp[N][N])
    
    
