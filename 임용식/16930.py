import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
graph = ["" for _ in range(n)]
check = [[float("inf") for _ in range(m)] for _ in range(n)]
for i in range(n):
    graph[i] = sys.stdin.readline().strip()
sr, sc, er, ec = map(int, sys.stdin.readline().split())
sr -= 1
sc -= 1
er -= 1
ec -= 1

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

q = deque()
q.append((sr, sc))
check[sr][sc] = 0
while len(q) > 0:
    cr, cc = q.popleft()

    if cr == er and cc == ec:
        break

    for i in range(4):
        nr = cr
        nc = cc
        for j in range(k):
            nr += dr[i]
            nc += dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                break
            if graph[nr][nc] == "#":
                break
            if check[nr][nc] <= check[cr][cc]:
                break

            next_cost = check[cr][cc] + 1
            if check[nr][nc] == float("inf"):
                check[nr][nc] = next_cost
                q.append((nr, nc))


print(-1 if check[er][ec] == float("inf") else check[er][ec])
