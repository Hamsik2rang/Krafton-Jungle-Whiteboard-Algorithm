import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    k=int(input())
    files=list(map(int,input().split()))
    dp=[0]*k
    
    # for i in range(1,k):
    #     for j in range(k-i):
            
