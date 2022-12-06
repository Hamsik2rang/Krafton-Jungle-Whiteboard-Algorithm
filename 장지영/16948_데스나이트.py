import sys
input = sys.stdin.readline
from collections import deque

N = int(input())    # 체스판 크기 N * N

firstR, firstC, lastR, lastC = map(int, input().split())

queue = deque()

move = [[-2, -1], [-2, +1], [0, -2], [0, +2], [+2, -1], [+2, +1]]
visited = [[0 for i in range(N)] for j in range(N)]

def bfs() : 
    queue.append([firstR, firstC, 0])
    visited[firstR][firstC] = 1
    
    while queue : 
        nowR, nowC, nowCount = queue.popleft()
        visited[nowR][nowC] = 1
        
        # 목적지 도착 
        if (nowR == lastR) and (nowC == lastC) : 
            return nowCount    
        
        for mov in range(6) : 
            dR, dC = move[mov]
            newR = nowR + dR
            newC = nowC + dC
            
            if (0 <= newR < N) and (0 <= newC < N) and (visited[newR][newC] == 0) : 
                queue.append([newR, newC, nowCount + 1])
                visited[newR][newC] = 1
    return -1

print(bfs())
