import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

W, H = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(H)]
visit = [[float('INF') for _ in range(W)] for _ in range(H)]

for i in range(H):
    graph[i] = list(sys.stdin.readline().strip())

C_pos= []
for i in range(H):
    for j in range(W):
        if graph[i][j] == 'C':
            C_pos.append((i,j))

sx, sy = C_pos[0]
ex, ey = C_pos[1]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# q = deque()
# q.append((start[0], start[1], 0, -1)) 
# # (row, col), count, direction
# # set first direction as '-1'

# def bfs(r2,c2):
#     global q
    
#     while len(q) > 0:
#         r, c, cur_count, cur_dir = q.popleft()

#         for i in range(4):
#             dr = [-1, 0, 1, 0]
#             dc = [0, -1, 0, 1]

#             nr = r + dr[i]
#             nc = c + dc[i]

#             if (
#                 nr >= 0
#                 and nr <= H-1
#                 and nc >= 0
#                 and nc <= W-1
#             ):
#                 if cur_dir == -1:
#                     if graph[nr][nc] != '*':
#                         visit[nr][nc] = cur_count
#                         q.append((nr,nc, cur_count, i))
#                 else:
#                     if graph[nr][nc] == '*':
#                         continue
#                     if abs(cur_dir - i) == 2:
#                         continue
#                     if cur_dir == i:
#                         if visit[nr][nc] > cur_count:
#                             visit[nr][nc] = cur_count
#                             q.append((nr,nc, cur_count, i))
#                     else:
#                         if visit[nr][nc] > cur_count+1:
#                             visit[nr][nc] = cur_count+1
#                             q.append((nr,nc, cur_count+1, i))

# bfs(final[0], final[1])
# print(visit[final[0]][final[1]])

def bfs(x,y):
    queue = deque([(x,y)])
    visit[x][y] = -1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while True:
                if not(0<=nx<H and 0<=ny<W): break

                if graph[nx][ny] == '*': break
                # 지나왔던 경로인데, 지금 경로로 가는 게 더 비효율적임
                if visit[nx][ny] < visit[x][y]+1: break

                queue.append((nx,ny))
                visit[nx][ny] = visit[x][y]+1
                nx += dx[i]
                ny += dy[i]

bfs(ex, ey)

print(visit[sx][sy])
