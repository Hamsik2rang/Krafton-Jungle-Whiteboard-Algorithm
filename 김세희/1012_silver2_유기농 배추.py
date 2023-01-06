import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]
t = int(input())
for _ in range(t):
    width, height, num = map(int, input().split())
    graph = [[0]*width for _ in range(height)]
    visited = [[False]*width for _ in range(height)]
    togo = deque([])
    for _ in range(num):
        x, y = map(int, input().split())
        togo.append((y,x))
        graph[y][x] = 1
    cnt = 0
    while(togo):
        row, col = togo.popleft()
        if visited[row][col]:
            continue
        cnt+=1
        visited[row][col] = True
        neighbor = deque([(row,col)])
        while(neighbor):
            row2, col2 = neighbor.popleft()
            for i in range(4):
                nr = dy[i] + row2
                nc = dx[i] + col2
                if 0<=nr<height and 0<=nc<width and not visited[nr][nc] and graph[nr][nc]:
                    visited[nr][nc] = True
                    neighbor.append((nr, nc))

    print(cnt)