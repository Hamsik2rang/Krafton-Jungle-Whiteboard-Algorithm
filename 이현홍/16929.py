import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(lambda x: ord(x) - 64, list(sys.stdin.readline().strip()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]

for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            Q = deque()
            Q.append((r, c))
            visited[r][c] = 1
            while Q:
                cr, cc = Q.popleft()
                for k in range(4):
                    nr, nc = cr + dr[k], cc + dc[k]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == arr[cr][cc]:
                        if visited[cr][cc] <= visited[nr][nc]:
                            print("Yes")
                            exit()
                        if not visited[nr][nc]:
                            visited[nr][nc] = visited[cr][cc] + 1
                            Q.append((nr, nc))
print("No")
