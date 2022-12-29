import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
off = list(list(map(int, input().split())) for _ in range(n))
cam = []
for i in range(n):
    for j in range(m):
        if 1 <= off[i][j] <= 5:
            cam.append((i, j, off[i][j]))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir = {1: [[0], [1], [2], [3]],
       2: [[0, 2], [1, 3]],
       3: [[0, 1], [1, 2], [2, 3], [3, 0]],
       4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
       5: [[0, 1, 2, 3]]}
cnt = sys.maxsize

def watch(r, c, d, mat):
    for i in d:
        nr, nc = r, c
        while True:
            nr += dr[i]
            nc += dc[i]
            if not (-1<nr<n and -1<nc<m) or mat[nr][nc] == 6:
                break
            if not mat[nr][nc]:
                mat[nr][nc] = 9

def dfs(dpt, off):
    global cnt
    mat = deepcopy(off)
    if dpt == len(cam):
        tmp = 0
        for l in mat:
            tmp += l.count(0)
        cnt = min(cnt, tmp)
        return
    r, c, x = cam[dpt]
    for d in dir[x]:
        watch(r, c, d, mat)
        dfs(dpt+1, mat)
        mat = deepcopy(off)

dfs(0, off)
print(cnt)