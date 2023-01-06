import sys
sys.stdin=open("input.txt", "r")
input=sys.stdin.readline

n,pn=map(int,input().split())
gl_lst=[[0]for _ in range(6+1)]

ans=0
for _ in range(n):
    l,p=map(int,input().split())
    if not gl_lst[l] or gl_lst[l][-1]<p:
        gl_lst[l].append(p)
        ans+=1
    else:
        while True:
            if (gl_lst[l][-1]<=p):
                if gl_lst[l][-1]<p:
                    gl_lst[l].append(p)
                    ans+=1
                break
            gl_lst[l]=gl_lst[l][:-1]
            ans+=1
            
print(ans)