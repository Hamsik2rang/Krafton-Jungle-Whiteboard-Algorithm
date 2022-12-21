import sys
sys.stdin=open("./input.txt", 'r')

import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
coin_map=[]
coin_location=[]
for y_idx in range(n):
    cc=list(input().strip())
    for x_idx in range(len(cc)):
        if cc[x_idx]=="o":
            coin_location.append([x_idx,y_idx])
    coin_map.append(cc)            

visit=[[False]*m for _ in range(n)]

dx=[0,1,0,-1] # 
dy=[-1,0,1,0] # 북 동 남 서

q=deque()
q.append(coin_location+[0])
visit[coin_location[0][1]][coin_location[0][0]]=True

print(coin_map)
print(coin_location)
print(visit)

# while q:
#     y,x, y2,x2,cnt=q.popleft() # x,y 기준으로 계속 움직일 것

#     for idx in range(4):
        # nx=x+dx[idx]
        # ny=y+dy[idx]
        
        # nx2=x2+dx[idx]
        # ny2=y2+dy[idx]        
        
        
        # if (0<=nx<=m and 0<=ny<=n) and not visit[nx][ny]:
        #     if not(0<=nx<=m and 0<=ny<=n):
        #         exit()
        #     else:            
        #         if coin_map[ny][nx]=="#":
        #             q.append([x,y,nx2,ny2])
                    
                