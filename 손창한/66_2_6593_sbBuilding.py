import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 1, 0, -1, 0, 0]
dc = [1, 0, -1, 0, 0, 0]
dl = [0, 0, 0, 0, 1, -1]

def bfs():
    que = deque()
    que.append((sl, sr, sc))
    while que:
        l, r, c = que.popleft()
        for i in range(6):
            nl = l + dl[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if -1<nl<L and -1<nr<R and -1<nc<C and not vis[nl][nr][nc]:
                if bld[nl][nr][nc] == '.' or bld[nl][nr][nc] == 'E':
                    vis[nl][nr][nc] = vis[l][r][c] + 1
                    que.append((nl, nr, nc))

while True:
    L, R, C = map(int, input().split())
    if L == 0:
        break
    bld = [[] * R for _ in range(L)]
    vis = [[[0] * C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            f = list(map(str, input().rstrip()))
            bld[i].append(f)
            for k in range(C):
                if f[k] == 'S':
                    sl, sr, sc = i, j, k
                elif f[k] == 'E':
                    el, er, ec = i, j, k
        input()
    bfs()
    if not vis[el][er][ec]:
        print("Trapped!")
    else:
        print(f"Escaped in {vis[el][er][ec]} minute(s).")