from multiprocessing.connection import answer_challenge
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def cycle(x,cnt,start_x):
    global ans

    for nx in graph[x]:
        # print(nx)
        if cnt>=3 and nx in start_x:
            print(start_x,cnt)
            return cnt
        
        if not visit[nx]:
            visit[nx]=1
            cycle(nx, cnt+1, start_x+[nx])
            visit[nx]=0


n=int(input())
graph=[[] for i in range(n+1)]
ans=[]
for _ in range(n):
    s,v=map(int,input().split())
    graph[s].append(v)
    graph[v].append(s)
    
for idx in range(1,n+1):
    visit=[0]*(n+1)
    visit[idx]=1
    cnt=cycle(idx,0,[idx]) 
    ans.append(cnt)
    print()
    
print(ans)
       
    
