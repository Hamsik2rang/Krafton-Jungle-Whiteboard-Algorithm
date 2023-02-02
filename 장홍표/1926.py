import sys

input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
Paper = [list(map(int, input().strip().split())) for _ in range(N)]
paints = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(paper, x, y):
    queue = deque()
    queue.append((x, y))
    paper[x][y] = 0
    paintA = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue
            if paper[new_x][new_y] == 1:
                paper[new_x][new_y] = 0
                queue.append((new_x, new_y))
                paintA += 1
    return paintA


for i in range(N):
    for j in range(M):
        if Paper[i][j] == 1:
            paints.append(bfs(Paper, i, j))

if len(paints) == 0:
    print("0")
    print("0")
else:
    print(len(paints))
    print(max(paints))
