"""
[문제] 백준-16930.달리기
* 입력
    - 체육관크기(n,m), 1초에 이동할 수 있는 칸의 최대개수(k)
    - 체육관 맵, 체육관 방문 여부
    => heap 이용해서 bfs로 탐색할 예정
        * 한 방향으로 k칸 이하로 간것은 다 heap에 넣어야 함
        * visit: 내가 그 위치로 갈수 있는 최소 시간 넣기?
        * nx,ny의 visit 값이 내 위치보다 크거나 같으면 못감??
    
* 출력
    - 도착 전 heap이 끝나버리면 -1 출력
    - heap에 다시 넣을 때 시간, nx, ny만 넣을 것
"""

import sys
from heapq import heappush, heappop
from collections import deque
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

n,m,k=map(int,input().split())
gym=[list(input().strip())for _ in range(n)]
visit=[[False]*(m) for _ in range(n)]
x1,y1,x2,y2=map(int,input().split())


dx=[-1,0,1,0]
dy=[0,1,0,-1]
def bfs(a,b): #시작 위치 받을 것
    x,y=a-1,b-1
    
    heap=[]
    heappush(heap,[0,x,y])    
    # heap=deque([])
    # heap.append([1,x,y])
    visit[x][y]=True
    
    while heap:
        s,x,y=heappop(heap)
        # s,x,y=heap.popleft()
        if x==x2-1 and y==y2-1:
            return print(s)
        
        # print(x,y)
        for i in range(4):
            nx=x
            ny=y
            for j in range(k):
                nx+=dx[i]
                ny+=dy[i]
                
                # print(nx,ny)
                if 0<=nx<n and 0<=ny<m :
                    if gym[nx][ny]=="." and not visit[nx][ny]:
                        visit[nx][ny]=True
                        heappush(heap,[s+1,nx,ny])
                        # heap.append([s+1,nx,ny])
                    elif gym[nx][ny]=="#":
                        break
                
        print(heap)
    
    return print(-1)

print(gym)
bfs(x1,y1)

            