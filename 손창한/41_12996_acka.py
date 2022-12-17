import sys
input = sys.stdin.readline

def solve(n, a, b, c):
    # escape
    if n == 0:
        return 1 if not (a or b or c) else 0
    if a < 0 or b < 0 or c < 0:
        return 0
    # if memo exist
    if dp[n][a][b][c] != -1:
        return dp[n][a][b][c]
    # rec
    dp[n][a][b][c] = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i+j+k == 0:
                    continue
                dp[n][a][b][c] += solve(n-1, a-i, b-j, c-k)
    dp[n][a][b][c] %= 1000000007
    return dp[n][a][b][c]

s, a, b, c = map(int, input().split())
dp = [[[[-1 for _ in range(s+1)] for _ in range(s+1)] for _ in range(s+1)] for _ in range(s+1)]
print(solve(s, a, b, c))
