import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Q = deque()


def shark():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 9:
                visit[r][c] = 0
                arr[r][c] = 0
                return (r, c, 0)

              
size = 2
eat = 0
active_time = 0
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
visit = [[1] * N for _ in range(N)]
Q.append(shark())
while Q:
    kill = []
    for _ in range(len(Q)):
        r, c, t = Q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] and arr[nr][nc] <= size:
                visit[nr][nc] = 0
                if 0 < arr[nr][nc] < size:
                    kill.append((nr, nc, t + 1))
                else:
                    Q.append((nr, nc, t + 1))
    if kill:
        eat += 1
        if eat == size:
            eat = 0
            size += 1
        Q = deque(sorted(kill)[:1])
        r, c, active_time = Q[0]
        visit = [[1] * N for _ in range(N)]
        arr[r][c] = 0
        visit[r][c] = 0

print(active_time)
