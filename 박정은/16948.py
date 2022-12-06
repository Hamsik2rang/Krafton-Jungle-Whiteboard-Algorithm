from collections import deque

def bfs(srcX,srcY,dstX,dstY):
    queue = deque()
    queue.append((srcX,srcY))
    visited[srcX][srcY] = True
    dx = [-2,-2,0,0,2,2 ]
    dy = [-1,1,-2,2,-1,1]

    while queue:
        x,y = queue.popleft()

        if x == dstX and y == dstY:
            return mtx[x][y]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < N and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                mtx[nx][ny] += mtx[x][y] + 1

    return -1

N = int(input())

mtx = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]

srcX,srcY,dstX,dstY = map(int, input().split())

print(bfs(srcX,srcY,dstX,dstY))

for one in mtx:
    print(one)
