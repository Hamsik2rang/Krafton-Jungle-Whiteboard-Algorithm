import sys
from heapq import heappush

papers = [(-1, -1)]
N = int(sys.stdin.readline())
for _ in range(N):
    n, m = map(int, sys.stdin.readline().split())
    papers.append((min(n, m), max(n, m)))
papers.sort()

dct = {i: [] for i in range(N + 1)}
mx = 0
heights = [papers[h][1] for h in range(N + 1)]
dct[0].append(-1)
for height in heights[1:]:
    for idx in range(mx, -1, -1):
        if dct[idx][0] <= height:
            heappush(dct[idx + 1], height)
            if mx < idx + 1:
                mx = idx + 1
            break

print(mx)
