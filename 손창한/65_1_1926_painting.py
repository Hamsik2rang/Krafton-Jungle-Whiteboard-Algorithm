import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(r, c):
    que = deque()
    que.append((r, c))
    vis[r][c] = True
    tmp = 1 # each area
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if -1<nr<n and -1<nc<m:
                if pnt[nr][nc] and not vis[nr][nc]:
                    vis[nr][nc] = True
                    que.append((nr, nc))
                    tmp += 1
    return tmp

n, m = map(int, input().split())
pnt = []
for _ in range(n):
    pnt.append(list(map(int, input().split())))
vis = [[False] * m for _ in range(n)]

cnt, mxp = 0, 0 # num of paintings, max area
for r in range(n):
    for c in range(m):
        if pnt[r][c] and not vis[r][c]:
            cnt += 1
            mxp = max(mxp, bfs(r, c))
print(cnt, mxp, sep='\n')