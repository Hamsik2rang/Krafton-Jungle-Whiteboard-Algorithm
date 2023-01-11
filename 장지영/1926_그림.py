import sys
input = sys.stdin.readline
from collections import deque

N, M = list(map(int, input().split()))

paper = []
for n in range(N) : 
    paper.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
picture = []
togo = deque()
for y in range(N) : 
    for x in range(M) : 
        if paper[y][x] == 1 : 
            count = 1
            paper[y][x] = 2 
            togo.append((y, x))
            
            
            while (togo) : 
                sy, sx = togo.popleft()
                for i in range(4) : 
                    newX = sx + dx[i]
                    newY = sy + dy[i]
                    
                    if (0 <= newX < M) and (0 <= newY < N) and (paper[newY][newX] == 1) : 
                        paper[newY][newX] = 2
                        togo.append([newY, newX])
                        count += 1
                        
            picture.append(count)

if not picture : 
    print(0)
    print(0)
else :                   
    print(len(picture))
    print(max(picture))
            