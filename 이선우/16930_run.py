import sys

sys.stdin = open("input.txt", "r")

import sys
import math

def BFS(step):
    global flag
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == step:
                if i>0 and matrix[i-1][j] == 0 and maze[i-1][j] == '.':
                    matrix[i-1][j] = step + 1
                if j>0 and matrix[i][j-1] == 0 and maze[i][j-1] == '.':
                    matrix[i][j-1] = step + 1
                if i<len(matrix)-1 and matrix[i+1][j] == 0 and maze[i+1][j] == '.':
                    matrix[i+1][j] = step + 1
                if j<len(matrix[i])-1 and matrix[i][j+1] == 0 and maze[i][j+1] == '.':
                    matrix[i][j+1] = step + 1
                if i<0 or j<0 or i>len(matrix)-1 or j>len(matrix[i])-1:
                    continue
                else:
                    flag = True
                    print('a')
                    return 

h, v, step = map(int, sys.stdin.readline().split())
maze = []

for _ in range(h):
    vertical = str(sys.stdin.readline().rstrip())
    maze.append([v for v in vertical])
    
matrix = [[0 for _ in range(v)] for _ in range(h)]
start_h, start_v, end_h, end_v = map(int, sys.stdin.readline().split())
matrix[start_h - 1][start_v - 1] = 1
move = 0
flag = False
print(matrix)
print(maze)

while matrix[end_h - 1][end_v - 1] == 0:
    move += 1
    BFS(move)
    if flag:
        break

if flag:
    print(-1)
else:
    i, j = end_h - 1, end_v - 1
    last_pos = (i , j)
    streak = 1
    end = matrix[i][j]
    path = []

    while end > 1:
        if i > 0 and matrix[i - 1][j] == end-1:
            if last_pos == (i + 1, j):
                streak += 1
            else:
                path.append(streak)
                streak = 1
            last_pos = (i, j)
            i, j = i - 1, j
            end-=1
        elif j > 0 and matrix[i][j - 1] == end-1:
            if last_pos == (i, j + 1):
                streak += 1
            else:
                path.append(streak)
                streak = 1
            last_pos = (i, j)
            i, j = i, j - 1
            end-=1
        elif i < len(matrix) - 1 and matrix[i + 1][j] == end-1:
            if last_pos == (i - 1, j):
                streak += 1
            else:
                path.append(streak)
                streak = 1
            last_pos = (i, j)
            i, j = i + 1, j
            end-=1
        elif j < len(matrix[i]) - 1 and matrix[i][j + 1] == end-1:
            if last_pos == (i, j - 1):
                streak += 1
            else:
                path.append(streak)
                streak = 1
            last_pos = (i, j)
            i, j = i, j + 1
            end -= 1
    path.append(streak)
    path.pop(0)

    ans = 0
    for movement in path:
        ans += math.ceil(movement / step)
    print(ans)