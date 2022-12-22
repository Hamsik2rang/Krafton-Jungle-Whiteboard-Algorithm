import sys
input = sys.stdin.readline
#늑대와 양

R, C = map(int, input().strip().split())
array = [input().strip() for _ in range(R)]

for i in range(R):
    for j in range(C):
        if array[i][j] == 'S':
            pass