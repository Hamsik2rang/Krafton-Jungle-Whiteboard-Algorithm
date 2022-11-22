import sys
from collections import deque
input = sys.stdin.readline

def bfs(sx, sy, ex, ey):
    queue = deque()
    queue.append((sx-1, sy-1))
    vis[sx-1][sy-1] = 0
    while queue:
        x, y = queue.popleft()
        if x == ex-1 and y == ey-1:
            return vis[x][y]
        for i in range(4):
            # move max k
            for l in range(1, k+1):
                nx = x + dx[i]*l
                ny = y + dy[i]*l
                # out of raddnge
                if not (-1<nx<n and -1<ny<m):
                    break
                # face wall
                if gym[nx][ny] == "#":
                    break
                # not visited
                if vis[nx][ny] == -1:
                    queue.append((nx, ny))
                    vis[nx][ny] = vis[x][y] + 1
                # keep go
                elif vis[nx][ny] == vis[x][y] + 1:
                    continue
                else:
                    break
    return -1

n, m, k = map(int, input().split())
gym = list(list(input().rstrip()) for _ in range(n))
sx, sy, ex, ey = map(int, input().split())
vis = [[-1] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
print(bfs(sx, sy, ex, ey))
