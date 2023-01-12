import sys
N = int(sys.stdin.readline().strip())
eggs = []
result = 0
for _ in range(N):
    S, W = map(int, sys.stdin.readline().strip().split())
    eggs.append([S, W])

def dfs(iter): 
  global result

  if iter == N: #다 돌았을 때 깨진 계란 개수세기
    cnt = 0
    for egg in eggs:
      if egg[0] <= 0:
        cnt += 1
    if cnt > result:
      result = cnt
    return

  if eggs[iter][0] <= 0:
    dfs(iter+1)
  else:
    flag = False
    for i in range(N):
      if i != iter and eggs[i][0] > 0:
        flag = True
        eggs[i][0] -= eggs[iter][1]
        eggs[iter][0] -= eggs[i][1]
        dfs(iter+1)
        eggs[i][0] += eggs[iter][1]
        eggs[iter][0] += eggs[i][1]
    
    if not flag: #계란이 전부 깨져버림
      dfs(N)

dfs(0)
print(result)
