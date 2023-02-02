import sys
input = sys.stdin.readline

n = int(input())
sl = "*"
i = 1
while i < n:
    e = [s*3 for s in sl]
    m = [s + " "*i + s for s in sl]
    sl = e+m+e
    i *= 3
print("\n".join(sl))
