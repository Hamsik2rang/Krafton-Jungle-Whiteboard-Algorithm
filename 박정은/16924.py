import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #row col

mtx =[]
visitedO = [[0] * M for _ in range(N)]
visitedC = [[0] * M for _ in range(N)]
lst = []

count = 0
for _ in range(N):
    mtx.append(input().strip())

for row in range(N):
    for col in range(M):
        if mtx[row][col] == '*':
            visitedO[row][col] = 1


for row in range(N):
    for col in range(M):

        if mtx[row][col] == '*':
            
            for i in range(0,49):
                flag = False
                drow = [0,0,-1-i,1+i]
                dcol = [-1-i,1+i,0,0]

                for j in range(4):
                    nrow = row + drow[j]
                    ncol = col + dcol[j]
                    if 0<= nrow < N and 0 <= ncol < M and mtx[nrow][ncol] == '*':
                        continue
                    else:
                        flag = True
                        break
                else:
                    for t in range(4):
                        nrow = row + drow[t]
                        ncol = col + dcol[t]
                        visitedC[nrow][ncol] = 1
                    visitedC[row][col] = 1
                    lst.append((row + 1, col + 1, i + 1))
                    count += 1

                if flag:
                    break
            


# for one in visitedO:
#     print(one)
# print()
# for one in visitedC:
#     print(one)

if visitedO == visitedC:
    print(count)
    for x,y,s in lst:
        print(x,y,s)
else:
    print(-1)
        


