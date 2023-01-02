import sys

sys.stdin = open("input.txt", "r")

import sys


T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    mn = 5000001
    K = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * K for _ in range(K)]
    # dp 2분할로 합치기 min
    print(mn)
