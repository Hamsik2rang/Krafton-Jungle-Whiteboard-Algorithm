import sys
input = sys.stdin.readline
#사이클 게임

N, M = map(int, input().split())
cl = [-1 for _ in range(N)]
counter = 0

for i in range(M):
    fir, sec = map(int, input().split())
    if(cl[fir] == -1 and cl[sec] == -1):
        cl[fir] = fir
        cl[sec] = fir
        # print(cl)
    elif(cl[fir] == -1 and cl[sec] != -1):
        cl[fir] = cl[sec]
        # print(cl)
    elif(cl[fir] != -1 and cl[sec] == -1):
        cl[sec] = cl[fir]
        # print(cl)
    else:
        if(cl[fir] == cl[sec]):
            counter = i+1
        # print(cl)
print(counter)