import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

n, c, t = map(int, input().split())
g = list(-int(input()) for _ in range(n))
heapify(g)
cnt = 0

for _ in range(t):
    h = heappop(g)
    if -h < c:
        heappush(g, h) 
        break
    elif -h == 1:
        heappush(g, h)
    else:
        h = -(-h//2)
        heappush(g, h) 
        cnt += 1

if -min(g) < c:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(-heappop(g))
