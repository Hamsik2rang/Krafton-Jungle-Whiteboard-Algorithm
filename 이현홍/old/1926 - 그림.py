import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
count = 0
mx = 0

for r in range(R):
    for c in range(C):
        if arr[r][c]:
            size = 0
            count += 1
            Q = deque([(r, c)])
            arr[r][c] = 0
            while Q:
                ir, ic = Q.popleft()
                size += 1
                for k in range(4):
                    nr = ir + dr[k]
                    nc = ic + dc[k]
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc]:
                        arr[nr][nc] = 0
                        Q.append((nr, nc))
            mx = max(size, mx)

print(count)
print(mx)
