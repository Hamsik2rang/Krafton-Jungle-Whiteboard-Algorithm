import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
visited = [[False]*(m+1) for _ in range(n+1)]
minMove = sys.maxsize

for row in range(1,n+1):
    graph[row] = [0]+list(map(int, input().split()))

h, w, startRow, startCol, goalRow, goalCol = map(int, input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def check(row, col):
    for rc in range(row, row+h):
        for cc in range(col, col+w):
            if graph[rc][cc]:
                # 벽
                return False

    return True

queue = deque([(startRow, startCol, 0)])

while(queue):
    row, col, move = queue.popleft()
    visited[row][col] = True

    if row==goalRow and col==goalCol:
        minMove = min(minMove, move)
        break

    for i in range(4):
        nr = row+dx[i]
        nc = col+dy[i]
        if nr<1 or nr>n or nc<1 or nc>m:
            continue
        if visited[nr][nc]:
            continue
        if nr+h-1<1 or nr+h-1>n or nc+w-1<1 or nc+w-1>m:
            continue
        if check(nr, nc):
            # 가도 되는 곳
            queue.append((nr, nc, move+1))
    

if minMove == sys.maxsize:
    print(-1)
else:
    print(minMove)