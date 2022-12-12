def dfs(x,y,t):
    if x == ax and y == ay:
        print('Yes')
        return True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1< nx < N and -1 < ny < M and mtx[nx][ny] == t and not visited[nx][ny]:
            visited[nx][ny] == True
            dfs(nx,ny,t)
            visited[nx][ny] == False
        elif not mtx[nx][ny] == t:
            return


dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, M = map(int,input().split())
mtx = []
for _ in range(N):
    mtx.append(input().strip())

visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        visited[i][j] == True
        ax,ay = i,j
        flag = False
        dfs(0,0,mtx[i][j])
        visited[i][j] == False
        if flag: break
    if flag: break
else: print("No")
