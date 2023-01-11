import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(sx, sy) : 
    togo = deque()
    togo.append([sx, sy])
    visited[sx][sy] = 2
    
    while togo : 
        x, y = togo.popleft()
        
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < M) and (0 <= ny < N) : 
                if (visited[nx][ny] == 1) : 
                    togo.append([nx, ny])
                    visited[nx][ny] = 2
    return 1
    


T = int(input())

for t in range(T) : # for each test case
    M, N, K = list(map(int, input().split()))
    visited = [[0 for n in range(N)] for m in range(M)]
    count_bugs = 0
    lettuce = []
    
    # lettuce position insert 
    for _ in range(K) : 
        flag = 0
        x, y = list(map(int, input().split()))
        visited[x][y] = 1
        lettuce.append([x, y])
        
    for l in lettuce : 
        if visited[l[0]][l[1]] == 1 : 
            count_bugs += bfs(l[0], l[1])
      
    print(count_bugs)
            
                