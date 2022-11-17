import sys
from heapq import heappush, heappop
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split())
graph=[list(map(int,list(input().strip())))for _ in range(n)]
# visitied=[[False]*(m) for _ in range(n)]
visitied=[[[False]*2 for _ in range(m)] for _ in range(n)]
# visitied[x][y][0] : 벽을 부수지 않고 지난 경로 유무, visitied[x][y][0] : 벽을 부수고 지난 경로 유무

def bfs():
    heap=[]
    heappush(heap,[1,0,0,0]) #부신벽 수, 걸음수, 현재위치(x,y)
    visitied[0][0][0]=True 
    
    while heap:
        a,wall,x,y=heappop(heap)
        
        if x==n-1 and y==m-1: # 목표지점 도착시 걸음 수 출력
            return print(a)
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and wall==0:
                    visitied[nx][ny][1]=True
                    heappush(heap,[a+1,1,nx,ny])

                elif graph[nx][ny]==0 and not visitied[nx][ny][wall]:
                    visitied[nx][ny][wall]=True
                    heappush(heap,[a+1,wall,nx,ny])
                
        print(heap)
    return print(-1)

bfs()
       
# -----21% 틀림 ----- visited 구현 잘못됨
# def bfs():
#     heap=[]
#     heappush(heap,[1,0,0,0]) #부신벽 수, 걸음수, 현재위치
#     visitied[0][0]=True
    
#     while heap:
#         a,wall,x,y=heappop(heap)
        
#         if x==n-1 and y==m-1: # 목표지점 도착시 걸음 수 출력
#             return print(a)
        
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if 0<=nx<n and 0<=ny<m:
#                 if graph[nx][ny]==1 and wall==0:
#                     visitied[nx][ny]=True
#                     heappush(heap,[a+1,1,nx,ny])
#                 elif graph[nx][ny]==0 and not visitied[nx][ny]:
#                     visitied[nx][ny]=True
#                     heappush(heap,[a+1,wall,nx,ny])
#         print(heap)
#     return print(-1)
# bfs()             
