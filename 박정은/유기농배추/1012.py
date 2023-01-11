import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]

    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if -1 < nrow < N and -1 < ncol < M and not visited[nrow][ncol] and mtx[nrow][ncol] == 1:
                queue.append((nrow, ncol))
                lst.remove((nrow, ncol))
                visited[nrow][ncol] = True


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    mtx = [[0]*M for _ in range(N)]
    lst = []
    count = 0
    for _ in range(K):
        gcol, grow = map(int, input().split())
        lst.append((grow, gcol))
        mtx[grow][gcol] = 1

    while lst:
        x, y = lst.pop()
        bfs(x, y)
        count += 1
    print(count)
