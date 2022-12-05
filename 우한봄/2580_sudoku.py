import sys
input=sys.stdin.readline

def checkRow(y, a):
    for i in range(n):
        if a == sudoku[y][i]:
            return False
    return True

def checkCol(x, a):
    for i in range(n):
        if a == sudoku[i][x]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == sudoku[ny+i][nx+j]:
                return False
    return True

def sudoku_q(idx):    
    for i in range(1,n+1):
        x=zero_lst[idx][0]
        y=zero_lst[idx][1]
        if checkCol(x,i) and checkRow(y,i) and checkRect(x,y,i): #조건문들: 해당 정수 i가 가로세로정사각형안에 들어가는지
            sudoku[y][x]=i
            if idx ==len(zero_lst)-1: # 성공!
                for i in range(n):
                    print(*sudoku[i])
                exit()
            else:
                sudoku_q(idx+1)
                sudoku[y][x]=0

n=9
sudoku=[]
zero_lst=[]
for y_idx in range(9):
    sudoku.append(list(map(int,input().split())))
    for x_idx in range(9):
        if sudoku[y_idx][x_idx]==0:
            zero_lst.append([x_idx,y_idx])
            
print(sudoku)
print(zero_lst)   

sudoku_q(0)


    
    