import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

#아기상어: 크기 작으면 먹고, 같으면 지나갈 수만, 크면 못 감
#거리가 가까운 물고기 부터. 거리가 같으면, 가장 위에 있는 물고기. 그것도 많으면, 가장 왼쪽.
N = int(sys.stdin.readline().strip())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

sx, sy = 0, 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            sx, sy = i, j
ssize = 2

def bfs(sx, sy, size):
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = 1
    temp_fish_list = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= nx < N and 0<= ny < N and visited[nx][ny] == 0:
                if graph[nx][ny] <= size:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cx][cy] + 1
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        temp_fish_list.append((nx, ny, distance[nx][ny]))
    return sorted(temp_fish_list, key=lambda x: (-x[2], -x[0], -x[1]))
        # for i in range(N):
        #     for j in range(N):
        #         if graph[i][j] < csize and graph[i][j] != 0:
        #             temp_fish_q.append((csize, abs(i-cx)+abs(j-cy), j, i))
        # temp_fish_q.sort()
        # while True:
        #     fish = temp_fish_q.popleft()
        #     fish_x, fish_y = fish[3], fish[2]

cnt = 0
result = 0

while True:
    fishes = bfs(sx, sy, ssize)
    if len(fishes) == 0:
        break

    nx, ny, distance = fishes.pop()
    result += distance
    graph[sx][sy] = 0
    graph[nx][ny] = 0

    sx, sy = nx, ny
    cnt += 1
    if cnt == ssize:
        ssize += 1
        cnt = 0

print (result)
