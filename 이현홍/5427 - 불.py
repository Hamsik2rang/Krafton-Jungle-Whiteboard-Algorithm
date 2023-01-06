import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

T = int(sys.stdin.readline())
dct = {"#": 10, ".": 0, "@": 1, "*": 5}
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def turn(Q, n):
    for _ in range(len(Q)):
        r, c = Q.popleft()
        if n == 1 and arr[r][c] != 1:
            continue

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] < n:
                arr[nr][nc] = n
                Q.append((nr, nc))
            if not (0 <= nr < h and 0 <= nc < w) and n == 1:
                global flag
                flag = 0
                return 0
    return Q


for tc in range(1, T + 1):
    w, h = map(int, sys.stdin.readline().split())
    human = deque()
    fire = deque()
    arr = [list(map(lambda x: dct[x], list(sys.stdin.readline().strip()))) for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if arr[r][c] == 1:
                human.append((r, c))
            elif arr[r][c] == 5:
                fire.append((r, c))

    time = 0
    flag = 1
    while human and flag:
        time += 1
        human = turn(human, 1)
        if flag:
            fire = turn(fire, 5)

    print("IMPOSSIBLE") if flag else print(time)
