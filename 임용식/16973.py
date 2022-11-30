import sys
from collections import deque


def is_stuck(row: int, col: int, height: int, width: int) -> bool:
    for r in range(row, row + height):
        if graph[r][col] == 1 or graph[r][col + width - 1]:
            return True
    for c in range(col, col + width):
        if graph[row][c] == 1 or graph[row + height - 1][c] == 1:
            return True
    return False


def bfs(start_row: int, start_col: int, height: int, width: int) -> int:
    global n, m
    global finish_col, finish_row

    dr = (-1, 0, 1, 0)
    dc = (0, -1, 0, 1)

    q = deque()
    q.append((start_row, start_col, 0))

    while len(q) > 0:
        cr, cc, cur_count = q.popleft()

        if cr == finish_row and cc == finish_col:
            return cur_count

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if (
                nr < 0
                or nc < 0
                or nr + height - 1 >= n
                or nc + width - 1 >= m
                or check[nr][nc]
            ):
                continue

            if is_stuck(nr, nc, height, width):
                continue

            check[nr][nc] = True
            q.append((nr, nc, cur_count + 1))

    return -1


class Quad:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
check = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))

height, width, start_row, start_col, finish_row, finish_col = map(
    int, sys.stdin.readline().split()
)

start_row -= 1
start_col -= 1
finish_row -= 1
finish_col -= 1

answer = bfs(start_row, start_col, height, width)
print(answer)
