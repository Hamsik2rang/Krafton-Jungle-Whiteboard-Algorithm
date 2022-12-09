import sys
from collections import deque
from heapq import heappush, heappop


def bfs(start_row: int, start_col: int) -> bool:
    global n, shark_level, shark_eat_count, shark_move_count, shark_pos

    dr = (-1, 0, 1, 0)
    dc = (0, -1, 0, 1)

    q = deque()
    pq = []
    check = [[False for _ in range(n)] for _ in range(n)]

    q.append((start_row, start_col, 0))
    check[start_row][start_col] = True
    while q:
        cr, cc, cur_count = q.popleft()

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if (
                nr < 0
                or nr >= n
                or nc < 0
                or nc >= n
                or check[nr][nc]
                or graph[nr][nc] > shark_level
            ):
                continue

            check[nr][nc] = True
            q.append((nr, nc, cur_count + 1))
            if graph[nr][nc] > 0 and graph[nr][nc] < shark_level:
                heappush(pq, (cur_count + 1, nr, nc))

    if len(pq) == 0:
        return False
    else:
        next_count, nr, nc = heappop(pq)
        shark_move_count += next_count
        shark_pos = [nr, nc]
        graph[nr][nc] = 0
        return True


n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
shark_pos = []
shark_level = 2
shark_eat_count = 0
shark_move_count = 0
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if graph[i][j] == 9:
            shark_pos = [i, j]
            graph[i][j] = 0


while True:
    result = bfs(shark_pos[0], shark_pos[1])
    if not result:
        break
    shark_eat_count += 1
    if shark_eat_count == shark_level:
        shark_level += 1
        shark_eat_count = 0

print(shark_move_count)
