import sys
from heapq import heapify, heappop, heappush

N, H, T = map(int, sys.stdin.readline().split())
heights = [-int(sys.stdin.readline()) for _ in range(N)]
heights.sort()

heapify(heights)
for t in range(T):
    giant = -(heappop(heights))
    if giant < H:
        print("YES")
        print(t)
        exit()
    giant = 1 if giant == 1 else giant // 2
    heappush(heights, -giant)

print("NO") if H <= -heights[0] else print("YES")
print(-heights[0]) if H <= -heights[0] else print(T)
