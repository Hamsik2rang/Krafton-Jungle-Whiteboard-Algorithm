import sys

sys.stdin = open("input.txt", "r")

import sys

def dfs(stack, index):
    global ans
    if len(stack) == len(cams):
        # change 0s in direction to #
        # check which is best with min(ans, temp)
        return

    y, x, cam = cams[index]
    if cam == 1:
        directions = [[0], [1], [2], [3]]
    elif cam == 2:
        directions = [[0, 2], [1, 3]]
    elif cam == 3:
        directions = [[0, 1], [1, 2], [2, 3], [3, 0]]
    elif cam == 4:
        directions = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
    else:
        directions = [[0, 1, 2, 3]]
    
    for direction in directions:
        stack.append(y, x, direction)
        dfs[stack, index + 1]
        stack.remove(y, x, direction)
y, x = map(int, sys.stdin.readline().split(' '))

office = [list(map(int, sys.stdin.readline().split())) for _ in range(y)]

cams = []
ans = 10**9

for i in range(y):
    for j in range(x):
        if 0 < office[i][j] < 6:
            cams.append([i, j, office[i][j]])
dfs([], 0)
