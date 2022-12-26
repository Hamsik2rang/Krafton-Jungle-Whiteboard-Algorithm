import sys
sys.stdin=open("input.txt","r");
input=sys.stdin.readline

R,C=map(int,input().split())
mapp=[]
sheep=[]

for idx in range(R):
    inp=list(input().strip())
    for x_idx in range(len(inp)):
        if inp[x_idx]=="S":
            sheep.append((idx,x_idx))
    mapp.append(inp)
        
            

def solution():
    for s in sheep:
        for direct in [[0,1],[1,0],[0,-1],[-1,0]]: # 우,하,좌,상
            ny=s[0]+direct[0]
            nx=s[1]+direct[1]
            if 0<=ny<R and 0<=nx<C:
                if mapp[ny][nx]=="W":
                    return False
                elif mapp[ny][nx]==".":
                    mapp[ny][nx]="D"
    
    return True

if not solution():
    print(0)
else:
    print(1)
    for i in range(len(mapp)):
        print(''.join(mapp[i]))
                
        