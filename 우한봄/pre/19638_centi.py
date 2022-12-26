import sys
sys.stdin=open("./input.txt", 'r')

import sys,heapq
from collections import deque
input=sys.stdin.readline

n,h,t=map(int,input().split())
# cnt=0

# giant=[]
# for _ in range(n):
#     heapq.heappush(giant, -int(input()))

# for i in range(t):
#     a=heapq.heappop(giant)
#     if abs(a)<h:
#         heapq.heappush(giant,a)
#         break
#     elif abs(a) ==1:
#         heapq.heappush(giant,a)
#     else: 
#         a= -(abs(a)//2)
#         heapq.heappush(giant,a)
#         cnt+=1

# if abs(min(giant))<h:
#     print(f"YES\n{cnt}")
# else:
#     print(f"NO\n{abs(heapq.heappop(giant))}")
    
# 틀렸습니다....
giant=[int(input()) for _ in range(n)]

def centi():
    giant.sort(reverse=True)
    dp=deque(giant)
    cnt=0

    while dp:
        bigest=dp.popleft()
        while bigest>=h and bigest!=1:
            bigest//=2
            cnt+=1
            if cnt>=t: 
                if dp: bigest=max(bigest,dp[0])
                break
        if cnt>=t: break
    
    return bigest,cnt
        
bigest,cnt=centi()
if bigest<h:
    print(f"YES\n{cnt}")
else:
    print(f"NO\n{bigest}")
    
    