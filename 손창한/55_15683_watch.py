import sys
input = sys.stdin.readline

def blind():
    vis = [[False for _ in range(m)] for _ in range(n)]
    for x in cam:
        r, c = x[0]
        vis[r][c] = True
        for d in x[1]:
            while True:
                r += dir[d][0]
                c += dir[d][1]
                if not (-1 < r < n and -1 < c < m):
                    break
                vis[r][c] = True
                if off[r][c] == 6:
                    break
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not vis[i][j]:
                cnt += 1
    return cnt

def dfs():
    vis = [False for _ in range(len(cam))]
    for x in cam:

n, m = map(int, input().split())
off = [[] for _ in range(n)]
cam = []
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(m):
        if l[j] == 1:
            cam.append([(i, j), (0, )])
        elif l[j] == 2:
            cam.append([(i, j), (0, 1)])
        elif l[j] == 3:
            cam.append([(i, j), (0, 2)])
        elif l[j] == 4:
            cam.append([(i, j), (0, 1, 2)])
        elif l[j] == 5:
            cam.append([(i, j), (0, 1, 2, 3)])
    off[i].extend(l)
# right, left, up, down
dir = ((0, 1), (0, -1), (-1, 0), (1, 0))
