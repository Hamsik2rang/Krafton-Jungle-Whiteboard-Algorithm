import sys
sys.stdin=open("input.txt","r")

def getPi(p):
    j=0
    pi=[0] * len(p)
    for i in range(1,len(p)):
        while j>0 and p[i] !=p[j]:
            j=pi[j-1]
        if p[i]==p[j]:
            j+=1
            pi[i]=j
    return pi

def kmp(t,p):
    ans=[]
    pi=getPi(p)

    j=0    
    for i in range(len(t)):
        while (j>0 and t[i]!=p[j]):
            j=pi[j-1]
        if t[i]==p[j]:
            j+=1
            if j==len(p):
                ans.append((i-j+1)+1)
                j=pi[j-1]

    return ans

t=input()
p=input()
matched=kmp(t,p)
print(len(matched))
if len(matched)!=0:
    print(*matched, sep=" ")