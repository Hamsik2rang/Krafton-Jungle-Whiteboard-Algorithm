import sys
from collections import deque


def bfs(row: int, col: int) -> bool:
    global graph, check, n, left, right

    dr = (-1, 0, 1, 0)
    dc = (0, -1, 0, 1)

    q = deque()
    q.append((row, col))
    sum_of_alliance_people = 0
    alliance = [(row, col)]
    while q:
        cr, cc = q.popleft()

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= n or check[nr][nc]:
                continue

            diff = abs(graph[cr][cc] - graph[nr][nc])
            if diff < left or diff > right:
                continue
            check[nr][nc] = True
            alliance.append((nr, nc))
            check[row][col] = True
            q.append((nr, nc))

    if len(alliance) == 1:
        return False

    for r, c in alliance:
        sum_of_alliance_people += graph[r][c]

    for r, c in alliance:
        graph[r][c] = sum_of_alliance_people // len(alliance)

    return True


def solution() -> bool:
    global n, check
    is_opened = False
    check = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if check[r][c]:
                continue
            result = bfs(r, c)
            if result:
                is_opened = True

    return is_opened


n, left, right = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
check = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))

answer = 0
while True:

    result = solution()
    if not result:
        break
    answer += 1

print(answer)
