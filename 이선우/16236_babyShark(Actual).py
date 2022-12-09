import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

n = int(sys.stdin.readline())
aquarium = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
size = 2
move_num = 0
container = 0
start_pos = [(index, row.index(9)) for index, row in enumerate(aquarium) if 9 in row]
aquarium[start_pos[0][0]][start_pos[0][1]] = 0
sx, sy = start_pos[0][0], start_pos[0][1]

while True:
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * n for _ in range(n)]
    flag = 1e9
    fish = []
    while q:
        x, y, count = q.popleft()

        if count > flag:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n: # 다음칸이 수족관 안에 있는지 확인
                continue

            if aquarium[nx][ny] > size or visited[nx][ny]: # 다음칸이 사이즈보다 크거나 이미 들른곳인지
                continue

            if aquarium[nx][ny] != 0 and aquarium[nx][ny] < size: # 다음칸이 먹을수 있으면 먹고 카운트를 플래그로
                fish.append((nx, ny, count + 1))
                flag = count
            visited[nx][ny] = True
            print(aquarium)
            q.append((nx, ny, count + 1))

    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        move_num += move
        container += 1
        aquarium[x][y] = 0
        if container == size:
            size += 1
            container = 0
        sx, sy = x, y
    else:
        break

print(move_num)