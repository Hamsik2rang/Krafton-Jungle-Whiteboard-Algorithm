import sys
sys.stdin = open('input.txt', 'r')

def update() -> None:
    global result
    
    team_L = []
    team_S = []

    for i in range(n):
        if lst[i]:
            team_L.append(i)
        else:
            team_S.append(i)
    
    sum_L = 0
    sum_S = 0

    for i in range(n//2):
        for j in range(i+1,n//2):
            sum_L += mtx[team_L[i]][team_L[j]] + mtx[team_L[j]][team_L[i]]
            sum_S += mtx[team_S[i]][team_S[j]] + mtx[team_S[j]][team_S[i]]

     
    result = min(result,abs(sum_L-sum_S))

    del team_L,team_S

    return 

def dfs(cur=0, x=0) -> None:
    if x == n//2:
        update()
        return
    
    for i in range(cur, n):
        lst[i] = True
        dfs(i+1, x+1)
        lst[i] = False
    
    return

n = int(input())

lst = [False] * n
result = 100_000_000

mtx = []
for _ in range(n):
    mtx.append(list(map(int,input().split())))

dfs()

print(result)