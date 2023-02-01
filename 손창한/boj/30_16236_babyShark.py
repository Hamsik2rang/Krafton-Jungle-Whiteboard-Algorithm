import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    vis = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((r, c))
    cnd = []
    vis[r][c] = 1
    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if -1<nr<n and -1<nc<n and not vis[nr][nc]:
                # empty or equal or smaller: go
                if mat[nr][nc] <= mat[r][c]:
                    queue.append((nr, nc))
                    vis[nr][nc] = vis[cr][cc]+1
                    # smaller: eat
                    if mat[nr][nc] and mat[nr][nc] < mat[r][c]:
                        cnd.append((vis[nr][nc]-1, nr, nc))
    return sorted(cnd, key=lambda x: (x[0], x[1], x[2]))

n = int(input())
mat, chk = [], []
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 9:
            chk.extend((i, j))
    mat.append(l)
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
cnt = 0

r, c = chk
size = 2
feed = 0
while True:
    mat[r][c] = size
    cnd = deque(bfs(r, c))
    if not cnd:
        break
    tmp, nr, nc = cnd.popleft()
    cnt += tmp
    feed += 1
    if size == feed:
        size += 1
        feed = 0
    mat[r][c] = 0
    r, c = nr, nc
print(cnt)
