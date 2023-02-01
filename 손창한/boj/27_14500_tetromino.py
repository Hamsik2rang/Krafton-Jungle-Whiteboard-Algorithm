import sys
input = sys.stdin.readline

def dfs(r, c, dpt, tmp):
    global cnt
    # escape(python)
    if tmp + mx*(4-dpt) <= cnt:
        return
    # escape
    if dpt == 4:
        cnt = max(cnt, tmp)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if -1<nr<n and -1<nc<m and not vis[nr][nc]:
            # case T
            if dpt == 2:
                vis[nr][nc] = True
                dfs(r, c, dpt+1, tmp+mat[nr][nc])
                vis[nr][nc] = False
            # case I, O, L, S
            vis[nr][nc] = True
            dfs(nr, nc, dpt+1, tmp+mat[nr][nc])
            vis[nr][nc] = False

n, m = map(int, input().split())
mat = list(list(map(int, input().split())) for _ in range(n))
vis = [[False for _ in range(m)] for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cnt = 0
mx = max(max(l) for l in mat)
for i in range(n):
    for j in range(m):
        vis[i][j] = True
        dfs(i, j, 1, mat[i][j])
        vis[i][j] = False
print(cnt)
