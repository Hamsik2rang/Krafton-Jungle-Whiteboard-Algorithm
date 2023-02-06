import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n=int(input())
graph=[[]for _ in range(n+1)]

for _ in range(n-1):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

ans=0
def dfs(root,deep):
    global ans
    if graph[root]:    
        for node in graph[root]:
            deep+=1
            graph[node].remove(root)
            print(graph)
            dfs(node,deep)
    else:
        print(deep)
        ans+=deep

dfs(1,0)
print(ans)
if (ans+1)%2==0:
    print("Yes")
else:
    print("N0")
    