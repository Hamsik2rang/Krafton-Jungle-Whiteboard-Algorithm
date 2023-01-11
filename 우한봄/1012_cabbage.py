import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def dfs(x,y):
    for direct in [[0,-1],[0,1],[-1,0],[1,0]]:
        nx=x+direct[0]
        ny=y+direct[1]
        
        if 0<=nx<m and 0<=ny<n and not visit[nx][ny]:
            if cbg_map[nx][ny]==1:
                visit[nx][ny]=True
                dfs(nx,ny) 
                    

for _ in range(int(input())):
    m,n,k=map(int,input().split())
    cbg_lst=[]
    cbg_map=[[0]*n for _ in range(m)]
    visit=[[False]*n for _ in range(m)]
    for i in range(k):
        x,y=map(int,input().split())
        cbg_map[x][y]=1
        cbg_lst.append([x,y])

    ans=0
    for c_idx in range(k):
        x,y=cbg_lst[c_idx]
        if not visit[x][y]:
            ans+=1
            dfs(x,y)
    print(ans)