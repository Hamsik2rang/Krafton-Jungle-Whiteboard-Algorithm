import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    size = 1
    matrix[y][x] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= w or new_y < 0 or new_y >= h:
                continue
            if matrix[new_y][new_x] == 1:
                size += 1
                matrix[new_y][new_x] = 0
                queue.append((new_x, new_y))
    return size

h, w = map(int, sys.stdin.readline().split())
matrix = []
ans = 0
size = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(h):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for x in range(w):
    for y in range(h):
        if matrix[y][x] == 1:
            temp = bfs(x, y)
            size = max(temp, size)
            ans += 1
print(ans)
print(size)