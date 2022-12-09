import sys
input = sys.stdin.readline

def dfs(r, c, br, bc, chk):
    # escape
    if vis[r][c]:
        print("Yes")
        exit()
    vis[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (-1<nr<n and -1<nc<m) or brd[nr][nc] != chk:
            continue
        if nr == br and nc == bc:
            continue
        dfs(nr, nc, r, c, chk)
    return False

n, m = map(int, input().split())
brd = list(list(input().strip()) for _ in range(n))
vis = [[False for _ in range(m)] for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

flg = False
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            flg = dfs(i, j, -1, -1, brd[i][j])
            if flg:
                break
print("No")
