import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    queue = deque()
    queue.append((0, 0, 0))
    vis[0][0][0] = 1
    while queue:
        r, c, w = queue.popleft()
        if r == n-1 and c == m-1:
            return vis[r][c][w]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if -1<nr<n and -1<nc<m:
                # mat[nr][nc] is not wall
                if not mat[nr][nc] and not vis[nr][nc][w]:
                    vis[nr][nc][w] = vis[r][c][w] + 1
                    queue.append((nr, nc, w))
                # mat[nr][nc] is wall and wall unbroken yet
                elif mat[nr][nc] and not w:
                    vis[nr][nc][1] = vis[r][c][0] + 1
                    queue.append((nr, nc, 1))
    return -1

n, m = map(int, input().split())
mat = list(list(map(int, list(input().rstrip()))) for _ in range(n))
# vis[r][c][w] = dist, not w: wall unbroken, w: wall broken
vis = [[[0] *2 for _ in range(m)] for _ in range(n)]
print(bfs())
