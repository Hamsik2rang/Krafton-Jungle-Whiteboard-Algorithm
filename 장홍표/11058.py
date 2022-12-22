import sys
input = sys.stdin.readline
#크리보드
# A버튼 / 전체선택 / 선택복사 / 붙여넣기
# 복붙 = 3step

N = int(input())
dp = [0 for _ in range(N+1)]
buff = [0 for _ in range(N+1)]

if(N<=6):
    print(N)
else:
    N = N-3
    dp[0:7] = [0, 1, 2, 3, 4, 5, 6]
    buff[3:7] = [0,0,0,3,3,3,3]
    for i in range(7, N+4):
        plus = dp[i-1] + 1
        multi = dp[i-3] * 2
        copy = dp[i-1] + max(buff)
        
        if(max(plus,multi,copy) == multi):
            dp[i] = multi
            buff[i] = dp[i-3]
        elif(max(plus,multi,copy) == copy):
            dp[i] = copy
            buff[i] = buff[i-1]
        else:
            dp[i] = plus
            buff[i] = buff[i-1]
        
    print(max(dp))
            
        
        