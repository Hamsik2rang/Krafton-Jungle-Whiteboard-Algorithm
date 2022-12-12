import sys

N = int(sys.stdin.readline().strip())
S = list(map(int, sys.stdin.readline().strip().split()))

max_N = 20
max_S = 100000

dp = [0 for _ in range(max_N*max_S + 1)]

def dfs(count:int, sum_S:int):
    if count == N:
        dp[sum_S] = True
        return
    
    dfs(count+1, sum_S + S[count])
    dfs(count+1, sum_S)

dfs(0, 0)

for i in range(1, max_N*max_S + 1):
    if dp[i] != True:
        print(i)
        break
