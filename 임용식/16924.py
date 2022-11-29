import sys


def check_cross(row: int, col: int, dr: int, dc: int, count: int) -> None:
    if count == 0:
        return
    check[row][col] = True
    nr = row + dr
    nc = col + dc
    check_cross(nr, nc, dr, dc, count - 1)


def dfs(row: int, col: int, dr: int, dc: int) -> int:
    global n, m
    if row < 0 or row >= n or col < 0 or col >= m or graph[row][col] != "*":
        return 0

    nr = row + dr
    nc = col + dc

    return 1 + dfs(nr, nc, dr, dc)


def solution(row: int, col: int) -> None:
    result = []
    dr = (-1, 0, 1, 0)
    dc = (0, -1, 0, 1)

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        result.append(dfs(nr, nc, dr[i], dc[i]))

    min_result = min(result)
    if min_result > 0:
        for i in range(min_result):
            answer.append([row + 1, col + 1, i + 1])
        check[row][col] = True
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            check_cross(nr, nc, dr[i], dc[i], min_result)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
check = [[False for _ in range(m)] for _ in range(n)]
answer = []
star_count = 0
for row in range(n):
    graph[row] = sys.stdin.readline().strip()

for row in range(n):
    for col in range(m):
        if graph[row][col] == "*":
            solution(row, col)


for row in range(n):
    for col in range(m):
        if graph[row][col] == "*" and not check[row][col]:
            print(-1)
            exit(0)
print(len(answer))
for row, col, size in answer:
    print(row, col, size)
