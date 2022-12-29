import sys

sys.stdin = open("input.txt", "r")

import sys

T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))
    income = 0
    mx = prices[-1]
    for idx in range(N-2, -1,-1):
        if prices[idx] < mx: income += mx-prices[idx]
        elif prices[idx] > mx: mx = prices[idx]
    print(income)
