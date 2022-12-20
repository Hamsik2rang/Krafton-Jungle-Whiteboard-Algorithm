import sys
from collections import deque
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n,m=map(int,input().split()) #높이,너비
visit=[[0]*m for _ in range(n)]
graph=[list(input().strip()) for _ in range(n)]

print(visit)
print(graph)

def dfs():
    q=deque()
    q.append(0,0,graph[0][0],0)
    visit[0][0]=1
    
    # color 판별 한 후, 간 방향에 있는 color 좌표의 순번과 3이상 차이가 나는가
    for i in range(n):
        for j in range(m):
            if not visit[i][j]:
                x,y,color=q.popleft()
                for direct in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nx=x+direct[0]
                    ny=y+direct[1]
            
                if 0<=nx<=n and 0<=ny<=m:
                    if color==graph[nx][ny]:
                        if 
                        q.append()
                    
            
    