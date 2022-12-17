import sys
from itertools import permutations, product
input = sys.stdin.readline

n = int(input())
scv = list(map(int, input().split()))
# set 3 scv if less
for _ in range(3-len(scv)):
    scv.append(0)
a, b, c = scv
dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
dp[a][b][c] = 1
# for i in range(60, -1, -1): for j in range(): for k in range():
for i, j, k in product(range(60, -1, -1), repeat=3):
    if dp[i][j][k]:
        for d in permutations((9, 3, 1), 3):
            # scv_i, j, k live or die
            ni = i-d[0] if i-d[0] > 0 else 0
            nj = j-d[1] if j-d[1] > 0 else 0
            nk = k-d[2] if k-d[2] > 0 else 0
            # if first memo or less than cnt
            if not dp[ni][nj][nk] or dp[ni][nj][nk] > dp[i][j][k]+1:
                dp[ni][nj][nk] = dp[i][j][k]+1
print(dp[0][0][0]-1)
