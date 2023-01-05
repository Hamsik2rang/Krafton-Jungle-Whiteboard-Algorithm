import sys

sys.stdin = open("input.txt", "r")


import sys
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def worm(y, x):
    Q = deque([(y, x)])
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]:
                arr[nr][nc] = 0
                Q.append((nr, nc))


T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    baechu = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
    for c, r in baechu:
        arr[r][c] = 1

    count = 0
    for c, r in baechu:
        if arr[r][c]:
            count += 1
            worm(r, c)
    print(count)
