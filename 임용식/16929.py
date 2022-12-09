import sys

sys.setrecursionlimit(10**6)


def dfs(cur_row: int, cur_col: int, last_row: int, last_col: int):
    global n, m, check, dr, dc, answer
    check[cur_row][cur_col] = True

    for i in range(4):
        nr = cur_row + dr[i]
        nc = cur_col + dc[i]

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if graph[nr][nc] != graph[cur_row][cur_col] or (
            last_row == nr and last_col == nc
        ):
            continue

        if check[nr][nc]:
            answer = True
            return

        dfs(nr, nc, cur_row, cur_col)
        if answer:
            return


n, m = map(int, sys.stdin.readline().split())
graph = ["" for _ in range(n)]
answer = False

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for i in range(n):
    graph[i] = sys.stdin.readline().strip()

for row in range(n):
    for col in range(m):
        check = [[False for _ in range(m)] for _ in range(n)]
        result = dfs(row, col, -1, -1)


print("Yes" if answer else "No")
