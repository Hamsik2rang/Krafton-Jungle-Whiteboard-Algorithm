
n = int(input())

dp = [i for i in range(0, 102)]

for i in range(6, 101):
    dp[i] = max(dp[i-3]*2, max(dp[i-4]*3, dp[i-5]*4)) # v를 한 번 누른경우 , 두 번 누른경우 , 세 번 누른경우
    
print(dp[n])
