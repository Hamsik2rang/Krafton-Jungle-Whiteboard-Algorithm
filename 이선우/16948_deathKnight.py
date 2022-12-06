import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

def bfs(x, y):
    move_x = [ 0, 0, -2, -2,  2, 2]
    move_y = [-2, 2, -1,  1, -1, 1]
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            print(matrix[x][y])
            break

        for i in range(6): 
            next_x = x + move_x[i]
            new_y = y + move_y[i]

            if 0 <= next_x < n and 0 <= new_y < n and matrix[next_x][new_y] == 0:
                matrix[next_x][new_y] = matrix[x][y] + 1
                queue.append([next_x, new_y])
    else:
        print(-1)

n = int(sys.stdin.readline())
start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]
bfs(start_x, start_y)