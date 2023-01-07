import sys

sys.stdin = open("input.txt", "r")

import sys

N, P, Q = map(int, sys.stdin.readline().split())
dct = {0: 1}


def number(n):
    m = dct.get(n, -1)
    if m != -1:
        return m
    else:
        l = number(n // P) + (number(n // Q))
        dct[n] = l
        return l


print(number(N))
