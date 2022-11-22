# 그래프 / 위상정렬/ 다이내믹 프로그래밍 
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())                            # 건물의 종류 수 

# ==========방향성 그래프 입력==============================

buildings = {}                              # 그래프
for _ in range(1, N + 1) : 
    buildings[_] = [0]
indegree = [0] * (N + 1)                    # 건물별 진입차수

for buildingNum in range(1, N + 1) : 
    # {건물번호} : [0] = 걸린시간  /  [1~] = 후위건물  / -1이 나오면 끝
    temp = list(map(int, input().split()))
    buildings[buildingNum][0] = temp[0]     # 걸린시간 입력
    for i in range(len(temp)) : 
        if i != 0 and temp[i] != -1 :       # 선행 건물들 
            buildings[temp[i]].append(buildingNum)  # 간선 연결
            indegree[buildingNum] += 1      # 현재 건물의 진입차수 증가

# print(buildings)
# print(indegree)
      
   
# ==========위상정렬 진행======================================
time = []
for k in range(N + 1) : time.append([0])
finalTime = [0] * (N + 1)
def topology_sort(buildings : dict, N : int) : 
    needQ = deque()
    # visited = []

    # 1. 진입차수가 0인 정점을 큐에 삽입
    for n in range(1, N + 1) : 
        if indegree[n] == 0 : 
            needQ.append(n)             # 대기큐에 삽입
        
    # 아직 방문대기가 남아있다면 
    while needQ : 
        current = needQ.popleft()
        # visited.append(current)         # 방문판정 
        
        # 방문한 노드 및 그 건물의 후위건물들에 시간추가 
        # 2. 현재 건물의 간선도 제거한다 
        for i in range(len(buildings[current])) : 
            if i == 0 :  
                for j in range(len(time[current])) : 
                    x = buildings[current][0]
                    time[current][j] += x
                finalTime[current] = max(time[current])
            else : 
                childBuilding = buildings[current][i]
                
                # 후위건물에 시간추가
                time[childBuilding].append(finalTime[current])
                # print(time[childBuilding])
                
                # 후위건물 진입차수 제거
                indegree[childBuilding] -= 1
                
                # 3. 후위건물 진입차수가 0이라면 방문대기에 넣는다 
                if indegree[childBuilding] == 0 : 
                    needQ.append(childBuilding)

topology_sort(buildings, N)
                    
# ===출력====
for bb in range(1, N + 1) : 
    print(finalTime[bb])
        
       
            
        
             

            
            
            


            
        