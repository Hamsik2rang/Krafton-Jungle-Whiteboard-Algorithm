import sys

sys.stdin = open("input.txt", "r")

import sys
import math
 
def solve():
    n = int(sys.stdin.readline())
    arr = [int(x) for x in input().split()]
    rst = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(1, n):
        for i in range(j-1, -1, -1):
            small = math.inf
            for k in range(j-i):
                small = min(small, rst[i][i+k] + rst[i+k+1][j])
            rst[i][j] = small + sum(arr[i:j+1])

    print(rst[0][n-1])
 
t = int(sys.stdin.readline())

for _ in range(t):
    solve()
