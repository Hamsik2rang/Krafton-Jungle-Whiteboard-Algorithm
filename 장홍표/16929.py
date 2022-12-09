import sys
input = sys.stdin.readline
from collections import deque
# Two Dots

N, M = map(int, input().strip().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0

array = [list(input().strip()) for _ in range(N)]
dp = [0 for _ in range(M) for _ in range(N)]

def bfs(x, y, array):
    q = deque()
    tmp = array[x][y]
    array[x][y] = 0
    q.append((x,y))
    while(q):
        q.popleft()
        for i in range(4):
            if((0<=(x+dx[i])<M) and (0<=(y+dy[i])<N)):
                if(array[x+dx[i]][y+dy[i]] == tmp):
                    q.append((x+dx[i],y+dy[i]))
                    array[x+dx[i]][y+dy[i]] = 0
                if(array[x+dx[i]][y+dy[i]] == 0):
                    answer = 1
                    break

for i in range(N):
    for j in range(M):
        if(array[i][j] != 0):
            bfs(i,j,array)

print(answer)