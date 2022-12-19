import sys
input = sys.stdin.readline
from collections import deque
# Two Dots


flag = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, M = map(int, input().strip().split())
array = [list(input().strip()) for _ in range(N)]
q = deque()
answer = 0

for i in range(N):
    for j in range(M):
        if(type(array[i][j])==str):
            q.append((i,j))
        while(q):
            y, x = q.popleft()
            array[y][x] = ord(array[y][x])
            count = 0
            for k in range(4):
                if(0<=(x+dx[k])<M and 0<=(y+dy[k])<N):
                    if(type(array[y+dy[k]][x+dx[k]])==str):
                        if(array[y][x] == ord(array[y+dy[k]][x+dx[k]])):
                            if(((y+dy[k]), (x+dx[k])) not in q):
                                q.append(((y+dy[k]), (x+dx[k])))
                    elif(type(array[y+dy[k]][x+dx[k]])==int):
                        if(array[y][x] == array[y+dy[k]][x+dx[k]]):
                            count += 1
                    if(count == 2):
                        answer = 1
                        break
            if(flag == 1):
                break
        if(flag == 1):
            break
    if(flag == 1):
        break
#test vscode
if(answer == 1):
    print("Yes")
else:
    print("No")