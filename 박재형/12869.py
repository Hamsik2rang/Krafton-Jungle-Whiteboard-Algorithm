import sys
# N is 1~3
N = int(sys.stdin.readline().strip())
# hp is 1~59
scv_hp = list(map(int, sys.stdin.readline().strip().split()))

dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]
# print(dp[0][0][0])

if N != 3:
    for i in range(3-N):
        scv_hp.append(0)

def sol(x:int, y:int, z:int):
    if x<0:
        return sol(0, y, z)
    if y<0:
        return sol(x, 0, z)
    if z<0:
        return sol(x, y, 0)
    
    if x==0 and y==0 and z==0:
        return 0

    if dp[x][y][z] != -1:
        return dp[x][y][z]
    
    temp = 60*60*60+1

    if temp > sol(x-9,y-3,z-1):
        temp = sol(x-9,y-3,z-1)
    if temp > sol(x-9,y-1,z-3):
        temp = sol(x-9,y-1,z-3)
    if temp > sol(x-3,y-9,z-1):
        temp = sol(x-3,y-9,z-1)
    if temp > sol(x-1,y-9,z-3):
        temp = sol(x-1,y-9,z-3)
    if temp > sol(x-1,y-3,z-9):
        temp = sol(x-1,y-3,z-9)
    if temp > sol(x-3,y-1,z-9):
        temp = sol(x-3,y-1,z-9)
    
    temp += 1
    dp[x][y][z] = temp
    return temp

sol(scv_hp[0], scv_hp[1], scv_hp[2])
print(dp[scv_hp[0]][scv_hp[1]][scv_hp[2]])

