import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

def bfs(matrix, x, y):
    queue = deque()
    queue.append((x,y))
    matrix[y][x] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= w or new_y < 0 or new_y >= h:
                continue
            if matrix[new_y][new_x] == 1:
                matrix[new_y][new_x] = 0
                queue.append((new_x, new_y))
    return

iter = int(sys.stdin.readline())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(iter):
    w, h, cabbage_count = map(int, sys.stdin.readline().split())
    matrix = [[0 for _ in range(w)] for _ in range(h)]
    ans = 0

    for _ in range(cabbage_count):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1

    for x in range(w):
        for y in range(h):
            if matrix[y][x] == 1:
                bfs(matrix, x, y)
                ans += 1
    print(ans)
