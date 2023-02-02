import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    que = deque()
    tmp = list()
    que.append((r, c))
    tmp.append((r, c))
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if -1<nr<N and -1<nc<N and not vis[nr][nc]:
                if L <= abs(mat[nr][nc] - mat[r][c]) <= R:
                    vis[nr][nc] = True
                    que.append((nr, nc))
                    tmp.append((nr, nc))
    return tmp

N, L, R = map(int, input().split())
mat = list(list(map(int, input().split())) for _ in range(N))
cnt = 0

while True:
    vis = [[False for _ in range(N)] for _ in range(N)]
    flg = False
    for i in range(N):
        for j in range(N):
            if not vis[i][j]:
                vis[i][j] = True
                uni = bfs(i, j)
                if len(uni) > 1:
                    flg = True
                    tmp = sum([mat[r][c] for r, c in uni]) // len(uni)
                    for r, c, in uni:
                        mat[r][c] = tmp
    if not flg:
        break
    cnt += 1
print(cnt)
