'''
1. 문제의 시간 제한은?
2초

2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
R,C<=500

3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
n^3???

4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
뭐든???

5. 왜 4라고 생각했는가?
널널해 보임

6. 풀이 sudo 코드
1) 그냥 늑대 앞뒤옆 주변에 다 울타리 쳐 두고 DFS 돌려봐서 양 먹을 수 있으면 0 출력하고 양까지 막아지면 그 맵을 출력하기
늑대 아예 없으면 바로 맵 출력하기


'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

r, c = map(int, input().split())
map = [[] for _ in range(r)]
wolves = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for row in range(r):
    map[row] = list(input().rstrip())
    for col in range(c):
        if map[row][col] == 'W':
            wolves.append((row, col))

if not wolves:
    print(1)
    for i in range(r):
        print("".join(map[i]))
    exit()

# 늑대 주변으로 울타리 치기
for row, col in wolves:
    for i in range(4):
        nr = row+dx[i]
        nc = col+dy[i]
        if 0<=nr<r and 0<=nc<c:
            if map[nr][nc] == '.':
                map[nr][nc] = 'D'

# 늑대 자리부터 양한테 갈 수 있는지 체크하는 dfs 함수
def dfs(row, col):
    if map[row][col] == 'S':
        return True
    
    flag = False
    for i in range(4):
        nr = row+dx[i]
        nc = col+dy[i]
        if 0<=nr<r and 0<=nc<c:
            if map[nr][nc] == 'D':
                continue
            if map[nr][nc] == 'S':
                return True
            if map[nr][nc] == '.':
                map[nr][nc] = 'V'
                flag = dfs(nr, nc)
                map[nr][nc] = '.'
                if flag: break
    
    return flag

flag = False
for row, col in wolves:
    flag = dfs(row, col)
    if flag:
        break

if flag:
    print(0)
else:
    print(1)
    for i in range(r):
        print("".join(map[i]))