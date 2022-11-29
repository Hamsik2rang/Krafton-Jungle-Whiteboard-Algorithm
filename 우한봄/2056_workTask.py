import sys
input=sys.stdin.readline

n=int(input())
# dp = [0 for _ in range(n)]
# graph = [[] for _ in range(n)]
time=[0]*n
rst=0
for idx in range(n):
    task=list(map(int,input().split()))
    if task[1]==0:
        time[idx]=task[0]
    else:
        maxx=0
        for p in task[2:]:
            maxx=max(maxx, time[p-1])                
        time[idx]=maxx+task[0]  
        print(maxx,time)
    
print(max(time))

    