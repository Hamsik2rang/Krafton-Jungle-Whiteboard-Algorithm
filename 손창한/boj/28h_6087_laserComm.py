import sys
from collections import deque
inf = sys.maxsize
input = sys.stdin.readline

def bfs(sr, sc):
    queue = deque()
    queue.append((sr, sc))
    vis[sr][sc] = -1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            while True:
                # out of mat
                if not (-1<nr<h and -1<nc<w):
                    break
                # face wall
                if mat[nr][nc] == "*":
                    break
                # too many mirror
                if vis[nr][nc] < vis[r][c]+1:
                    break
                queue.append((nr, nc))
                vis[nr][nc] = vis[r][c]+1
                # keep go
                nr += dr[i]
                nc += dc[i]

w, h = map(int, input().split())
mat, chk = [], []
for i in range(h):
    l = input().rstrip()
    for j in range(w):
        if l[j] == "C":
            chk.append((i, j))
    mat.append(list(l))
(sr, sc), (er, ec) = chk
vis = [[inf for _ in range(w)] for _ in range(h)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
bfs(sr, sc)
print(vis[er][ec])
