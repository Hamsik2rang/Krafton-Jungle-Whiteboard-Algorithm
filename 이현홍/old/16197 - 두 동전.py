import sys
from collections import deque


def check(rn1, nc1, nr2, nc2):
    if not (0 <= nr1 < N and 0 <= nc1 < M) and not (0 <= nr2 < N and 0 <= nc2 < M):
        return "PASS"
    if 0 <= nr1 < N and 0 <= nc1 < M and 0 <= nr2 < N and 0 <= nc2 < M:
        return "APPEND"
    if ((not 0 <= nr1 < N and 0 <= nc1 < M) and (0 <= nr2 < N and 0 <= nc2 < M)) or ((0 <= nr1 < N and 0 <= nc1 < M) and (not 0 <= nr2 < N and 0 <= nc2 < M)):
        return "END"


N, M = map(int, sys.stdin.readline().split())

coins = []
arr = [[1] * M for _ in range(N)]

for r in range(N):
    line = sys.stdin.readline().rstrip()
    for c in range(M):
        if line[c] == "o":
            coins.append((r, c))
        elif line[c] == "#":
            arr[r][c] = 0

r1, c1 = coins[0]
r2, c2 = coins[1]

Q = deque()
Q.append((r1, c1, r2, c2, 0))

visit = [[1] * 2121 for _ in range(2121)]
visit[r1 * 100 + c1][r2 * 100 + c2] = 0

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

while Q:
    r1, c1, r2, c2, t = Q.popleft()
    if 10 <= t:
        print(-1)
        exit()
    for k in range(4):
        nr1, nc1, nr2, nc2 = r1 + dr[k], c1 + dc[k], r2 + dr[k], c2 + dc[k]
        result = check(nr1, nc1, nr2, nc2)
        if result == "PASS":
            continue
        elif result == "APPEND":
            if not arr[nr1][nc1]:
                nr1, nc1 = r1, c1
            if not arr[nr2][nc2]:
                nr2, nc2 = r2, c2

            if visit[nr1 * 100 + nc1][nr2 * 100 + nc2]:
                visit[nr1 * 100 + nc1][nr2 * 100 + nc2] = 0
                Q.append((nr1, nc1, nr2, nc2, t + 1))
        else:
            print(t + 1)
            exit()

print(-1)
