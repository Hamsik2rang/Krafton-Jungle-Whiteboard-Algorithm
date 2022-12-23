import sys

sys.stdin = open("input.txt", "r")

import sys

R, C = map(int, sys.stdin.readline().split())
office = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
sagak = 0
cctv = []
for r in range(R):
    for c in range(C):
        if 0 < office[r][c] < 6:
            cctv.append((r, c))
        elif not office[r][c]:
            sagak += 1
mn = sagak

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def Eye(r, c, d, t):
    nr = r
    nc = c
    new = 0
    while True:
        nr += dr[d]
        nc += dc[d]
        if not (0 <= nr < R and 0 <= nc < C) or office[nr][nc] == 6:
            break
        else:
            if t:
                if office[nr][nc] == 0:
                    new += 1
                if office[nr][nc] <= 0:
                    office[nr][nc] -= 1
            else:
                if office[nr][nc] < 0:
                    office[nr][nc] += 1
    return new


def DFS(idx=0, sagak=sagak):
    if idx == len(cctv):
        global mn
        mn = min(mn, sagak)
        return
    r, c = cctv[idx]
    camera = office[r][c]
    d = [4, 2, 4, 4, 1]
    for k in range(d[camera - 1]):
        clear = 0
        if camera == 1:
            clear += Eye(r, c, k, 1)
            DFS(idx + 1, sagak - clear)
            Eye(r, c, k, 0)
        elif camera == 2:
            clear += Eye(r, c, k, 1) + Eye(r, c, (k + 2) % 4, 1)
            DFS(idx + 1, sagak - clear)
            Eye(r, c, k, 0), Eye(r, c, (k + 2) % 4, 0)
        elif camera == 3:
            clear += Eye(r, c, k, 1) + Eye(r, c, (k + 1) % 4, 1)
            DFS(idx + 1, sagak - clear)
            Eye(r, c, k, 0), Eye(r, c, (k + 1) % 4, 0)
        elif camera == 4:
            clear += Eye(r, c, k, 1) + Eye(r, c, (k + 1) % 4, 1) + Eye(r, c, (k + 2) % 4, 1)
            DFS(idx + 1, sagak - clear)
            Eye(r, c, k, 0), Eye(r, c, (k + 1) % 4, 0), Eye(r, c, (k + 2) % 4, 0)
        elif camera == 5:
            clear += Eye(r, c, 0, 1) + Eye(r, c, 1, 1) + Eye(r, c, 2, 1) + Eye(r, c, 3, 1)
            DFS(idx + 1, sagak - clear)
            Eye(r, c, 0, 0), Eye(r, c, 1, 0), Eye(r, c, 2, 0), Eye(r, c, 3, 0)


DFS()

print(mn)
