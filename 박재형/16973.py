import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[0 for _ in range(M+1)] for _ in range(N+1)]
visited = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    input_line = list(map(int, sys.stdin.readline().split()))
    graph[i] = [False] + input_line

def checkWall(h:int, w:int, curr_row, curr_col):
    for i in range(curr_row, curr_row+h):
        if graph[i][curr_col] == 1 or graph[i][curr_col+w-1] == 1:
            return True
    for j in range(curr_col, curr_col+w):
        if graph[curr_row][j] == 1 and graph[curr_row+h-1][j] == 1:
            return True
    return False

H, W, row_start, col_start, row_end, col_end = map(int, sys.stdin.readline().strip().split())

if not(1<=row_start<=N-H+1) or not(1<=col_start<=M-W+1) or not(1<=row_end<=N-H+1) or not(1<=col_end<=M-W+1):
    print(-1)
else:
    q = deque()
    q.append((row_start, col_start))

    dc = [1, -1, 0, 0]
    dr = [0, 0, 1, -1]

    while q:
        (curr_r, curr_c) = q.popleft()
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if 1<= nr and nr <= (N-H+1) and 1 <= nc and nc <= (M-W+1) and visited[nr][nc] == 0 and not checkWall(H, W, nr, nc):
                visited[nr][nc] = 1 + visited[curr_r][curr_c]
                q.append((nr, nc))
                if nr == row_end and nc == col_end:
                    break

    visited[row_start][col_start] = 1

    if visited[row_end][col_end] != 0:
        print(visited[row_end][col_end])
    else:
        print(-1)
