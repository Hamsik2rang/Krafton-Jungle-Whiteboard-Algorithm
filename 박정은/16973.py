import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

from collections import deque

def bfs(row,col) -> int:
    queue = deque()
    queue.append((row,col))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        if x == destX-1 and y == destY-1:
            return visited[x][y]

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            for p in range(n-1,-1,-(n-1)):
                flag = False
                for pp in range(m):
                    if -1 < ny+pp < M and -1 < nx+p < N and not visited2[nx][ny] and not mtx[nx+p][ny+pp]:
                        continue
                    else:
                        flag = True
                        break
                if flag:
                    break
            else:
                for p in range(0,n):
                    for pp in range(m-1,-1,-(m-1)):
                        if -1 < ny+pp < M and -1 < nx+p < N and not visited2[nx][ny] and not mtx[nx+p][ny+pp]:
                            continue
                        else:
                            flag = True
                            break
                    if flag:
                        break
                else:
                    queue.append((nx,ny))
                    visited[nx][ny] += visited[x][y] + 1
                    visited2[nx][ny] = True
    return -1

N, M = map(int, input().split())

mtx = []
visited = [[0] * M for _ in range(N)]
visited2 = [[False] * M for _ in range(N)]
for _ in range(N):
    mtx.append(list(map(int,input().split())))

n, m, srcX, srcY, destX, destY = map(int, input().split())

print(bfs(srcX-1,srcY-1))

for one in mtx:
    print(one)

print()

for one in visited:
    print(one)

print()

for one in visited2:
    print(one)