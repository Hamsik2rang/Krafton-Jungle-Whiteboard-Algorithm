import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    que = deque()
    que.append((r, c))
    frm[r][c] = False
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if -1<nr<n and -1<nc<m and frm[nr][nc]:
                frm[nr][nc] = False
                que.append((nr, nc))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    frm = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        c, r = map(int, input().split())
        frm[r][c] = True
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    cnt = 0
    for r in range(n):
        for c in range(m):
            if frm[r][c]:
                bfs(r, c)
                cnt += 1
    print(cnt)