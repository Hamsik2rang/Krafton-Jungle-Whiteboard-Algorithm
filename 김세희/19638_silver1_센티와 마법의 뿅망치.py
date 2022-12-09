'''
센티키랑 가장 큰 거인 키랑 비교해서 센티키보다 작으면 반복 멈춘다..
센티키보다 크면 반으로 줄여서 다시 넣는다..
'''

import sys
import heapq

input = sys.stdin.readline

n,h,t = map(int, input().split())
giants = []
answer = -1
success = False
hammer = 0

for _ in range(n):
    heapq.heappush(giants, -int(input()))

while(True):
    maximum = -heapq.heappop(giants)
    
    if h>maximum:
        answer = hammer
        success = True
        break
   
    else:
        if hammer==t or maximum==1:
            answer = maximum
            break
        heapq.heappush(giants, -(maximum//2))
        hammer+=1
       

print('YES' if success==True else 'NO')
print(answer)