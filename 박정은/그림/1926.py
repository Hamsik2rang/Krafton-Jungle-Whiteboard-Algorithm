import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]

    visited[x][y] = True

    cnt = 1

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if -1 < nrow < M and -1 < ncol < N and not visited[nrow][ncol] and mtx[nrow][ncol] == 1:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = True
                cnt += 1
    return cnt


M, N = map(int, input().split())

mtx = []
for _ in range(M):
    mtx.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(M)]

count = 0
getsu = 0


for row in range(M):
    for col in range(N):
        if not visited[row][col] and mtx[row][col] == 1:
            count = max(count, bfs(row, col))
            getsu += 1

if count :
    print(getsu)
    print(count)
else:
    print(0)
    print(0)
    
