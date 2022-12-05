import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
coins = []
for i in range(n):
    graph[i] = sys.stdin.readline().strip()
    for j in range(m):
        if graph[i][j] == "o":
            coins.append([i, j])

answer = 0

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

q = deque()
q.append((coins[0], coins[1], 0))
while len(q) > 0:
    coin1, coin2, cur_count = q.popleft()

    if cur_count >= 10:
        print(-1)
        break

    for i in range(4):
        nr1 = coin1[0] + dr[i]
        nc1 = coin1[1] + dc[i]
        nr2 = coin2[0] + dr[i]
        nc2 = coin2[1] + dc[i]

        if (
            nr1 >= 0
            and nr1 < n
            and nr2 >= 0
            and nr2 < n
            and nc1 >= 0
            and nc1 < m
            and nc2 >= 0
            and nc2 < m
        ):
            if graph[nr1][nc1] == "#":
                nr1 = coin1[0]
                nc1 = coin1[1]
            if graph[nr2][nc2] == "#":
                nr2 = coin2[0]
                nc2 = coin2[1]
            q.append(([nr1, nc1], [nr2, nc2], cur_count + 1))
        elif (nr1 < 0 or nr1 >= n or nc1 < 0 or nc1 >= m) and (
            nr2 < 0 or nr2 >= n or nc2 < 0 or nc2 >= m
        ):
            continue
        else:
            print(cur_count + 1)
            exit(0)
