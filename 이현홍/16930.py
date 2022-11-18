import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
gym = [[] for _ in range(N)]

for idx in range(N):
    for s in sys.stdin.readline().strip():
        if s == ".":
            gym[idx].append(1)
        else:
            gym[idx].append(0)

r1, c1, r2, c2 = map(lambda x: int(x) - 1, sys.stdin.readline().split())


visit = [[0xFFFFFF for _ in range(M)] for __ in range(N)]
Q = deque()
Q.append((r1, c1))
visit[r1][c1] = 0
dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
while Q:
    r, c = Q.popleft()

    for i in range(4):
        for l in range(1, K + 1):
            nr = r + dir_r[i] * l
            nc = c + dir_c[i] * l
            if 0 <= nc < M and 0 <= nr < N:
                if gym[nr][nc] and visit[r][c] + 1 < visit[nr][nc]:
                    if nr == r2 and nc == c2:
                        print(visit[r][c] + 1)
                        exit()
                    t = visit[r][c] + 1
                    visit[nr][nc] = t
                    Q.append((nr, nc))
                elif gym[nr][nc] and visit[r][c] + 1 == visit[nr][nc]:
                    continue
                else:
                    break

print(-1)
