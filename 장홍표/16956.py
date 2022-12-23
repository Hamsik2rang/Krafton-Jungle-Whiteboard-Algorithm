import sys
input = sys.stdin.readline
#늑대와 양

R, C = map(int, input().strip().split())
array = [input().strip() for _ in range(R)]
answer = 1

for i in range(R):
    for j in range(C):
        if array[i][j] == 'S':
            if(0<i):
                if (array[i-1][j] == 'W'):
                    answer = 0
                    break
            if(i<R-1):
                if (array[i+1][j] == 'W'):
                    answer = 0
                    break
            if(0<j):
                if (array[i][j-1] == 'W'):
                    answer = 0
                    break
            if(j<C-1):
                if (array[i][j+1] == 'W'):
                    answer = 0
                    break
    if(answer == 0):
        break

                
# 출력부분
if(answer):
    print(answer)
    for i in range(R):
        array[i] = array[i].replace('.',"D")
        print(array[i])
else:
    print(0)