import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

def bfs(y, x):
    global size
    global container
    global start_pos
    global count
    move_x = [ 0, -1, 0, 1]
    move_y = [-1,  0, 1, 0]
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        if aquarium[x][y] != 0 and aquarium[x][y] < size:
            aquarium[x][y] = 0
            container += 1
            if container == size:
                container = 0
                size += 1
            count += matrix[x][y]
            start_pos = [(x, y)]
            return True

        for i in range(4): 
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            if 0 <= next_x < iter and 0 <= next_y < iter:
                if aquarium[next_x][next_y] <= size and matrix[next_x][next_y] == 0:
                    matrix[next_x][next_y] = matrix[x][y] + 1
                    queue.append([next_x, next_y])
    else:
        return False

iter = int(sys.stdin.readline())
matrix = [[0 for _ in range(iter)] for _ in range(iter)]
aquarium = []
size = 2
container = 0
count = 0
flag = True

for _ in range(iter):
    aquarium.append(list(map(int, sys.stdin.readline().split())))

start_pos = [(index, row.index(9)) for index, row in enumerate(aquarium) if 9 in row]
aquarium[start_pos[0][0]][start_pos[0][1]] = 0

while flag:
    flag = bfs(start_pos[0][0], start_pos[0][1])
    matrix = [[0 for _ in range(iter)] for _ in range(iter)]
else:
    print(count)
