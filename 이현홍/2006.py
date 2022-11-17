import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

arr = [tuple(map(int, tuple(sys.stdin.readline().strip()))) for _ in range(N)]
dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]


def Que(row, col):
    Q = deque()
    Q.append((row, col))
    visit = [[0 for _ in range(M)] for __ in range(N)]
    visit[row][col] = 1

    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dir_r[k]
            nc = c + dir_c[k]

            if 0 <= nr < N and 0 <= nc < M:
                if not visit[nr][nc]:
                    visit[nr][nc] = visit[r][c] + 1
                    if not arr[nr][nc]:
                        Q.append((nr, nc))
    return visit


v1 = Que(0, 0)
v2 = Que(N - 1, M - 1)

mn = 0xFFFFFF
for r in range(N):
    for c in range(M):
        if v1[r][c] and v2[r][c]:
            if v1[r][c] + v2[r][c] - 1 < mn:
                mn = v1[r][c] + v2[r][c] - 1

print(mn) if mn < 0xFFFFFF else print(-1)
