'''
상하좌우 다 별인 점 찾아서 출력
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(input())
answer = []

for row in range(n):
    for col in range(m):
        tile = board[row][col]
        if tile != ".":
            leng = 1
            dx=[0,leng,-leng,0]
            dy=[leng,0,0,-leng]
            flag = True
            tochange = []
            for i in range(4):
                if 0<=row+dx[i]<n and 0<=col+dy[i]<m:
                    if board[row+dx[i]][col+dy[i]] == '.':
                        flag = False
                        break
                else:
                    flag = False
                    break

            if not flag:
                continue

            for i in range(4):
                if 0<=row+dx[i]<n and 0<=col+dy[i]<m:
                    if board[row+dx[i]][col+dy[i]] == '*':
                        tochange.append((row+dx[i], col+dy[i]))

            # 십자가 중심임 .. 크기 구해야 함
            while(True):
                j = leng+1
                tempx = [0,j,-j,0]
                tempy = [j,0,0,-j]
                flag = True
                for e in range(4):
                    nr = row+tempx[e]
                    nc = col+tempy[e]
                    if 0<=nr<n and 0<=nc<m:
                        if board[nr][nc] == '.':
                            flag = False
                            break
                    else:
                        flag=False
                        break

                if not flag: break
                
                for e in range(4):
                    nr = row+tempx[e]
                    nc = col+tempy[e]
                    if 0<=nr<n and 0<=nc<m:
                        if board[nr][nc] == '*':
                            tochange.append((nr, nc))
                    else:
                        flag=False
                        break
                leng = j
            for r,c in tochange:
                board[r][c] = '+'
            board[row][col] = '+'
            answer.append((row, col, j))

check = True
for row in range(n):
    for col in range(m):
        if board[row][col]=='*':
            check = False
            break
if check:
    print(len(answer))
    for one, two, three in answer:
        print(one+1, two+1, three-1)
else:
    print(-1)