import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline


for _ in range(int(input())):
    n=int(input())
    stocks=list(map(int,input().split()))
    
    max_stock=0
    ans=0
    for s in reversed(stocks):
        if s>=max_stock:
            max_stock=s
        else:
            ans+=(max_stock-s)
    print(ans)
    