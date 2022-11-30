import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
r_map=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*(m+1) for _ in range(n+1)]

h,w,sy,sx,fy,fx=map(int,input().split())

dx=[0,1,0,-1] # 
dy=[-1,0,1,0] # 북 동 남 서

y,x=sy-1,sx-1
q=deque()
q.append([y,x,0])
visited[y][x]=True


while q:
    y,x,cnt=q.popleft()
    if x==fx-1 and y==fy-1:
        print(cnt)
        break

    for idx in range(4):
        nx=x+dx[idx]
        ny=y+dy[idx]
        
        if (0<=nx and nx+(w-1)<=m-1 and 0<=ny and ny+(h-1)<=n-1 and not visited[ny][nx]):
            go=True
            for h_idx in range(h):
                if (r_map[y+h_idx][nx:(nx+w)] != [0]*w):
                    go=False
                    break
            if go:
                visited[ny][nx]=True
                q.append([ny,nx,cnt+1])
    # print(q)
                
                    

