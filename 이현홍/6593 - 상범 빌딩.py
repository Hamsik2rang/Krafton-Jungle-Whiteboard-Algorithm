import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

dr = [0, 0, 0, 0, 1, -1]
dc = [0, 0, 1, -1, 0, 0]
dh = [1, -1, 0, 0, 0, 0]


def BFS(Q):
    while Q:
        h, r, c, t = Q.popleft()
        for k in range(6):
            nh, nr, nc = h + dh[k], r + dr[k], c + dc[k]
            if 0 <= nh < H and 0 <= nr < R and 0 <= nc < C:
                if building[nh][nr][nc] == ".":
                    building[nh][nr][nc] = "#"
                    Q.append((nh, nr, nc, t + 1))
                elif building[nh][nr][nc] == "E":
                    return t
    return 0


def start(H, R, C):
    for h in range(H):
        for r in range(R):
            for c in range(C):
                if building[h][r][c] == "S":
                    building[h][r][c] = "#"
                    return BFS(deque([(h, r, c, 1)]))


while True:
    H, R, C = map(int, sys.stdin.readline().split())
    if H == R == C == 0:
        break
    building = []
    for _ in range(H):
        building.append([list(sys.stdin.readline().rstrip()) for _ in range(R)])
        sys.stdin.readline()

    t = start(H, R, C)
    print(f"Escaped in {t} minute(s).") if t else print("Trapped!")
