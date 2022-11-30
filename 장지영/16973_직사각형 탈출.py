import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

board = [[0 for c in range(M + 1)] for r in range(N + 1)]

# (row, col)칸은 board[row][col]
for n in range(1, N + 1) : 
    line = list(map(int, input().split()))
    for m in range(1, M + 1) : 
        board[n][m] = line[m - 1]
# print(board)
    
height, width, startR, startC, finalR, finalC = map(int, input().split())

visited = [[0 for i in range(M + 1)] for j in range(N + 1)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 1이 있다면 왼쪽위로 w, h만큼 못간다
# 왼쪽 윗칸이 못가는 곳은 방문처리 미리 해준다 
for n in range(1, N + 1) :
    for m in range(1, M + 1) : 
        if board[n][m] == 1 : 
            for i in range(n, n-height, -1) : 
                if (i < 1) :
                    break
                for j in range(m, m-width, -1) : 
                    if (j < 1) : 
                        break
                    visited[i][j] = 1



def bfs() :
    queue = deque()
    queue.append([startR, startC, 0])
    visited[startR][startC] = 1
    while queue : 
        nowR, nowC, cnt = queue.popleft()
        # print(nowR, nowC, cnt)
        
        # 목적지 도달하면 끝
        if (nowC == finalC) and (nowR == finalR) : 
            # print(cnt)
            return cnt
        
        # 이동 
        for k in range(4) : 
            newC = nowC + dc[k]
            newR = nowR + dr[k]
            
            # 다음 단계가 가능한지 검사 
            if (newC < 1) or (newC > M - width + 1) or (newR < 1) or (newR > N - height + 1) : 
                continue
            elif (visited[newR][newC]) : # 방문처리 한 곳이면 통과
                continue
            else : 
                # 방문처리 및 count 
                queue.append([newR, newC, cnt + 1])
                visited[newR][newC] = 1

    # 끝까지 찾았는데 못찾았으면 return -1
    return -1
  
print(bfs())   



