import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((sr-1, sc-1))
    vis[sr-1][sc-1] = 1
    while queue:
        r, c = queue.popleft()
        if r == fr-1 and c == fc-1:
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<=n-h and 0<=nc<=m-w:
                if not (pfs[nr+h][nc+w] - pfs[nr][nc+w] - pfs[nr+h][nc] + pfs[nr][nc]) > 0:
                    if not vis[nr][nc]:
                        queue.append((nr, nc))
                        vis[nr][nc] = vis[r][c] + 1

n, m = map(int, input().split())
mat = list(list(map(int, input().split())) for _ in range(n))
h, w, sr, sc, fr, fc = map(int, input().split())
vis = [[0 for _ in range(m)] for _ in range(n)]
# prefix_sum list
pfs = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        pfs[i][j] = mat[i-1][j-1] + pfs[i-1][j] + pfs[i][j-1] - pfs[i-1][j-1]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
bfs()
print(vis[fr-1][fc-1]-1)
