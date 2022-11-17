import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
graph = [None for _ in range(n)]
check = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
for i in range(n):
    graph[i] = sys.stdin.readline().strip()

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)


q = deque()
q.append((0, 0, False))
check[0][0][0] = check[1][0][0] = 1
while len(q) > 0:
    is_broken, cr, cc = q.popleft()

    if cr == n - 1 and cc == m - 1:
        break

    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue

        if graph[nr][nc] == "1" and is_broken == 1:
            continue

        next_broken = is_broken

        if graph[nr][nc] == "1" and is_broken == 0:
            next_broken = 1

        if (
            check[next_broken][nr][nc] > 0
            and check[next_broken][nr][nc] <= check[is_broken][cr][cc] + 1
        ):
            continue
        check[next_broken][nr][nc] = check[is_broken][cr][cc] + 1
        q.append((next_broken, nr, nc))

if check[0][n - 1][m - 1] > 0 and check[1][n - 1][m - 1] > 0:
    print(min(check[0][n - 1][m - 1], check[1][n - 1][m - 1]))
elif check[0][n - 1][m - 1] > 0:
    print(check[0][n - 1][m - 1])
elif check[1][n - 1][m - 1] > 0:
    print(check[1][n - 1][m - 1])
else:
    print(-1)
