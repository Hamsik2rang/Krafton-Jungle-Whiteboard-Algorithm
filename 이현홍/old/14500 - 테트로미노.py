import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

V = [[1] * M for _ in range(N)]
visit = [[1] * M for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def tetro(r, c, s, n):
    if n == 4:
        global result
        if result < s:
            result = s
        return
    else:
        tmp.append((r, c))
        visit[r][c] = 0

        mx = -1
        for (tr, tc) in tmp:
            for k in range(4):
                nr, nc = tr + dr[k], tc + dc[k]
                if 0 <= nr < N and 0 <= nc < M and V[nr][nc] and mx < arr[nr][nc] and visit[nr][nc]:
                    tetro(nr, nc, s + arr[nr][nc], n + 1)
        visit[r][c] = 1
        tmp.pop()


result = -1
tmp = []
for r in range(N):
    for c in range(M):
        V[r][c] = 0
        tetro(r, c, arr[r][c], 1)

print(result)
