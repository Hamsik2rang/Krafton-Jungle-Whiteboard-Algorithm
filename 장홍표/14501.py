import sys
input = sys.stdin.readline

N = int(input())  #날짜
dp = [0 for _ in range(N+1)]  #금액 dp
daypay = [] #소요시간, 성과급 list

for _ in range(N):
    daypay.append(list(map(int, input().strip().split())))
#소요시간 및 성과급 input

for i in reversed(range(N)): #마지막날 부터 dp (해당일자 기준 최대한 많은 돈)
    if daypay[i][0] <= N-i:  #소요시간이 퇴사일 까지보다 남은기간보다 커야 함
        dp[i] = max(dp[i+(daypay[i][0]):]) + daypay[i][1]
    else:
        dp[i] = max(dp)

print(max(dp))
