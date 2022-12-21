# import sys
# sys.stdin=open("./input.txt", 'r')

import sys
import heapq
from collections import deque
input=sys.stdin.readline

sea_map=[]
fish=[]
n=int(input())
for idx in range(n):
    a_lst=list(map(int,input().split()))
    for idx2 in range(len(a_lst)):
        if a_lst[idx2]==9:
            shark=[idx2,idx]
            a_lst[idx2]=0

    sea_map.append(a_lst)

def bfs(start):
    pq=[]
    heapq.heappush(pq,[0,2,start])
        
    direct=[[0,-1],[-1,0],[0,1],[1,0]]
    
    # while pq:
    for _ in range(5):
        step,size,xy=heapq.heappop(pq)
        
        size_lst=list(set(sum(sea_map,[])))
        # size_lst.remove(0)
        
        print(sea_map)
        print(size_lst)
        if size_lst[0]>size or (len(size_lst)==0 and size_lst[-1]==0):
            return step 
        
        x,y=xy[0],xy[1]
        for i in range(4):
            nx,ny=x+direct[i][0],y+direct[i][1]
            if (0<=nx<n) and (0<=ny<n):
                if sea_map[ny][nx]<size:
                    sea_map[ny][nx]=0
                    heapq.heappush(pq,[step-1,size,[nx,ny]])
                elif sea_map[ny][nx]==size:
                    sea_map[ny][nx]=0
                    heapq.heappush(pq,[step-1,size+1,[nx,ny]])
        
        print(pq)

print(shark)                    
print(-bfs(shark))
        
    
                    
                    
                
                
            
        
    #물고기 위치를 받음
    # 위쪽, 왼쪽 순으로 돌음
    # 조건 1. 나보다 큰 물고기를 만나면: 못가고 다른 방향으로
    # 조건 2. 나랑 같은 물고기를 만나면: 위치 업데이트
    # 조건 3. 나보다 작은 물고기를 만나면: 위치 및 크기 업데이트
    # 한 cycle에 스텝 +1
    # 전체에서 나보다 작은 물고기가 없다면 return
    
    
        