import sys
input = sys.stdin.readline
from collections import deque
##데스나이트
N = int(input())
i = 1
q = deque()

array = [[0 for _ in range(N)] for _ in range(N)]
sr, sc, er, ec = map(int, input().strip().split())

#움직인공간이 맵 밖인지 체크
#움직인공간이 이미 지나간 장소인지 체크
def Move(row, col, array, q):
    #큐에 집어넣기
    q.append((row,col))
    while(q):
        (r, c) = q.popleft()
        if (r-2)>=0 and (r-2) < N and (c+1)>=0 and (c+1) < N:
            if array[r-2][c+1] == 0:
                array[r-2][c+1] = array[r][c] + 1
                q.append((r-2,c+1))
        if (c+2)>=0 and (c+2) < N:
            if array[r][c+2] == 0:
                array[r][c+2] = array[r][c] + 1
                q.append((r,c+2))
        if (r-2)>=0 and (r-2) < N and (c-1)>=0 and (c-1) < N:
            if array[r-2][c-1] == 0:
                array[r-2][c-1] = array[r][c] + 1
                q.append((r-2,c-1))
        if (r+2)>=0 and (r+2) < N and (c+1)>=0 and (c+1) < N:
            if array[r+2][c+1] == 0:
                array[r+2][c+1] = array[r][c] + 1
                q.append((r+2,c+1))
        if (c-2)>=0 and (c-2) < N:
            if array[r][c-2] == 0:
                array[r][c-2] = array[r][c] + 1
                q.append((r,c-2))
        if (r+2)>=0 and (r+2) < N and (c-1)>=0 and (c-1) < N:
            if array[r+2][c-1] == 0:
                array[r+2][c-1] = array[r][c] + 1
                q.append((r+2,c-1))
#test
Move(sr,sc,array,q)
if array[er][ec] == 0:
    print(-1)
else:
    print(array[er][ec])