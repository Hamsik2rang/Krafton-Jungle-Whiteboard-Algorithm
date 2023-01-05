import sys, copy
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n,m=map(int,input().split())
mapp=[]
visit=[[False]*m]*n

cctv=[]
cctv_cnt=0

ans=int(10e9)
direction=[[1,0],[-1,0],[0,1],[0,-1]]
mode=[[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], 
      [[0, 2], [2, 1], [1, 3], [3, 0]],
      [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], 
      [[0, 1, 2, 3]]]
    
def dfs(mp,cnt):
    global ans
    
    tmp=copy.deepcopy(mp)
    if cnt==cctv_cnt:
        c=0
        for i in tmp:
            c+=i.count(0)
        ans=min(ans,c)
        # if ans==15:
        #     for idx in range(len(tmp)):
        #         print(" ".join(str(tmp[idx])))
        #     print()
        return
    
    c_type,y,x=cctv[cnt]
    for i in mode[c_type]:
        watch(y,x,i,tmp)
        dfs(tmp,cnt+1)
        tmp=copy.deepcopy(mp)        
    

def watch(y,x,mode,tmp):
    for md in mode:
        ny=y
        nx=x
        while True:            
            ny+=direction[md][1]
            nx+=direction[md][0]
            if 0<=ny<n and 0<=nx<m and tmp[ny][nx]!=6:
                if tmp[ny][nx]==0:
                    tmp[ny][nx]='#'
            else:
                break
                     
for y_idx in range(n):
    lst=list(map(int,input().split()))
    mapp.append(lst)
    for x_idx in range(len(lst)):
        if lst[x_idx]!=0 and lst[x_idx]!=6:
            cctv_cnt+=1
            cctv.append((lst[x_idx],y_idx,x_idx))

dfs(mapp,0)
print(ans)