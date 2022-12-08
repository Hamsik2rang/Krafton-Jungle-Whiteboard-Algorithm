import sys
from heapq import heappush, heappop

n, h, t = map(int, sys.stdin.readline().split())
giant = []
answer = 0

for i in range(n):
    heappush(giant, -int(sys.stdin.readline()))

for i in range(t):
    front = heappop(giant)
    if front * -1 < h:
        print("YES", i, sep="\n")
        exit(0)
    if front * -1 > 1:
        front = (-1 * front) // 2 * -1
    heappush(giant, front)

front = -1 * heappop(giant)
if front >= h:
    print("NO", front, sep="\n")
else:
    print("YES", t, sep="\n")
