import sys

#print(-1) if solution does not exist
N, M = map(int, sys.stdin.readline().strip().split())
graph = [ [] for _ in range(N+1)]

for i in range(1,N+1):
    input_line = [0] + list(sys.stdin.readline().strip())
    graph[i]=input_line

counter_list = []

for row in range(2,N):
    for col in range(2,M):
        if graph[row][col] == '*':
            if graph[row-1][col]=="*" and graph[row+1][col]=="*"\
                and graph[row][col-1]=="*" and graph[row][col+1]=="*":
                counter_list.append((row,col))

def checkMaxCross(i:int, j:int):
    k=1
    while 1<=i-k and i+k<=N and 1<=j-k and j+k<=M:
        if (graph[i-k][j]=="*" or graph[i-k][j]=="x") and\
            (graph[i+k][j]=="*" or graph[i+k][j]=="x") and\
            (graph[i][j-k]=="*" or graph[i][j-k]=="x") and\
            (graph[i][j+k]=="*" or graph[i][j+k]=="x"):
            graph[i-k][j]="x"
            graph[i+k][j]="x"
            graph[i][j-k]="x"
            graph[i][j+k]="x"
            graph[i][j]='x'
        else:
            break
        k+=1
    return k-1

result = []

for (row, col) in counter_list:
    size = checkMaxCross(row, col)
    result.append((row,col,size))

tmp=0
for i in range(1,N+1):
    tmp+=graph[i].count('*')

if tmp != 0:
    print(-1)
else:
    print(len(result))
    for elmt in result:
        print(elmt[0],elmt[1],elmt[2])

    
