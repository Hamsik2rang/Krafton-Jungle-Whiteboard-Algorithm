'''
시뮬레이션 하기
'''

import sys
input = sys.stdin.readline
from collections import deque
import copy

n = int(input())

board = [[]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
size = 2
second = 0
fishes = 0

dr = [-1,0,1,0]
dc = [0,-1,0,1]

now = (-1,-1)
for i in range(n):
    board[i] = list(map(int, input().split()))
    for j in range(n):
        if not board[i][j]: continue
        if board[i][j]==9:
            now = (i,j)
        else:
            fishes+=1
        

def bfs():
    global now, size, second, fishes
    # queue 구성 : [(현재 상어 row, 현재 상어 col), 현재 board, 현재 visited, 현재 size, 현재 second, 현재 먹은 물고기 수, 남은 물고기 수]
    queue = deque([[now, copy.deepcopy(board), copy.deepcopy(visited), size, second, 0, fishes]])
    time = 0
    while(queue):
        now, tboard, tvisit, tsize, tsec, eat, left = queue.popleft()
        nowR, nowC = now
        tvisit[nowR][nowC] = True
        if left==0:
            # 물고기 다 먹었으면
            print(tsec)
            return
        flag = True
        
        for i in range(4):
            newvisit = copy.deepcopy(tvisit)
            nr = nowR + dr[i]
            nc = nowC + dc[i]
            if nr<0 or nr>=n or nc<0 or nc>=n: continue
            if not tboard[nr][nc] and not tvisit[nr][nc]:
                # 빈칸
                newvisit[nr][nc] = True
                queue.append([(nr, nc), tboard, newvisit, tsize, tsec + 1, eat, left])
                flag = False
            elif tsize>tboard[nr][nc] and not tvisit[nr][nc]:
                # 갈 수 있고, 물고기 먹음
                newboard = copy.deepcopy(tboard)
                newboard[nr][nc] = 0
                newvisit = copy.deepcopy(visited)
                newEat = eat+1
                newSize = tsize
                if newEat == newSize:
                    # 먹은 수랑 현재 사이즈랑 같으면
                    newSize += 1
                    newEat = 0
              
                queue.append([(nr, nc), newboard, newvisit, newSize, tsec+1, newEat, left-1])
                flag = False

            elif tsize==tboard[nr][nc] and not tvisit[nr][nc]:
                # 갈 수 있고, 물고기 먹을 순 없음
                newvisit[nr][nc] = True
                queue.append([(nr, nc), tboard, newvisit, tsize, tsec+1, eat, left])
                flag = False
        if flag:
            time = tsec
          
    print(time)

bfs()