import sys
from collections import deque
input = sys.stdin.readline

def bfs(r1, c1):
    queue = deque()
    queue.append((r1, c1))
    brd[r1][c1] = 0
    while queue:
        r, c = queue.popleft()
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            if -1<nr<n and -1<nc<n and brd[nr][nc] == -1:
                queue.append((nr, nc))
                brd[nr][nc] = brd[r][c]+1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
brd = [[-1 for _ in range(n)] for _ in range(n)]
dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]
bfs(r1, c1)
print(brd[r2][c2])
