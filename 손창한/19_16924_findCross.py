import sys
input = sys.stdin.readline

def bfs(r, c):
    for l in range(1, min(n, m)):
        flg = True
        for i in range(4):
            nr = r + l*dr[i]
            nc = c + l*dc[i]
            if not (-1<nr<n and -1<nc<m and mat[nr][nc] == "*"):
                flg = False
                break
        if not flg:
            break
        ret.append((str(r+1)+" "+str(c+1)+" "+str(l)))
        for i in range(4):
            nr = r + l*dr[i]
            nc = c + l*dc[i]
            vis[nr][nc] = 0
        vis[r][c] = 0

n, m = map(int, input().split())
mat = list(list(input().rstrip()) for _ in range(n))
vis = [[0 for _ in range (m)] for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
ret = []
cnt = 0
# set vis
for i in range(n):
    for j in range(m):
        if mat[i][j] == "*":
            vis[i][j] = 1
# bfs
for i in range(n):
    for j in range(m):
        if mat[i][j] == "*":
            bfs(i, j)
# chk
for i in range(n):
        cnt += sum(vis[i])
if cnt:
    print(-1)
else:
    print(len(ret))
    print(*ret, sep="\n")
