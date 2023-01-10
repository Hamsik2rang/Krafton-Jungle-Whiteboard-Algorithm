import sys; input = sys.stdin.readline
from collections import deque

q = deque()

N, M = map(int, input().strip().split())
Paper = [list(input().strip().split()) for _ in range(N)]
paintC = 0
paintAmax = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    for j in range(M):
        if(Paper[i][j]=='1'):
            q.append((i,j))
            paintC += 1
            paintA = 0
            while(q):
                I,J = map(int, q.popleft())
                if(Paper[I][J]=='0'):
                    break
                else:
                    Paper[i][j] = '0'
                    for k in range(4):
                        new_x = J + dx[k]
                        new_y = I + dy[k]
                        if new_x < 0 or new_x >= M or new_y < 0 or new_y >= N:
                            continue
                        if Paper[new_y][new_x] == '1':
                            Paper[new_y][new_x] = '0'
                            q.append((new_y, new_x))
                    paintA += 1
                
                paintAmax = max(paintAmax,paintA)
                    
print(Paper)
if(paintC == 0):
    print("0")
    print("0")
else:
    print(paintC)
    print(paintAmax)