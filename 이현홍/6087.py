import sys
from collections import deque


def exchange(s: str):
    if s == ".":
        return 1
    else:
        return 0 if s == "*" else 2


C, R = map(int, sys.stdin.readline().split())
arr = [list(map(lambda x: exchange(x), list(sys.stdin.readline().strip()))) for _ in range(R)]
visit = [[[0xFFFFF] * 4 for _ in range(C)] for _ in range(R)]

machines = []
for r in range(R):
    for c in range(C):
        if arr[r][c] == 2:
            machines.append((r, c))

Sr, Sc = machines[0]
Fr, Fc = machines[1]

Q = deque()

for od in range(4):
    Q.append((Sr, Sc, od))
    visit[Sr][Sc][od] = 0

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]
while Q:
    r, c, od = Q.popleft()
    for d in range(4):
        if od + d == 3:
            continue
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc]:
            v = visit[r][c][od] + 1 if od != d else visit[r][c][od]
            if v < visit[nr][nc][d]:
                visit[nr][nc][d] = v
                Q.append((nr, nc, d))

print(min(visit[Fr][Fc]))
