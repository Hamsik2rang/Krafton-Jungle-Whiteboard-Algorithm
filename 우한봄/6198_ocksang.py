import sys
from bisect import bisect_right
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

ans=0
stack=[]
for _ in range(int(input())):
    o=int(input())
    if not stack:
        stack.insert(0,o)
    else:
        if stack[0]<=o:
           s_idx=bisect_right(stack, o)
           stack=stack[s_idx:]
        stack.insert(0,o)
    ans+=len(stack)-1
    print(stack)

print(ans)