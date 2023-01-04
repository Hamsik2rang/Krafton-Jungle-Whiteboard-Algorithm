import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, P = list(map(int, input().split()))

# stack : 116052KB, 356ms
finger = 0

guitar = {}
for _ in range(1, 7) : 
    guitar[_] = [0, ]

for n in range(N) : 
    line, prat = list(map(int, input().split()))
    while guitar[line][-1] > prat : 
        guitar[line].pop()
        finger += 1     # 하나씩 손가락을 뗀다 
          
    if guitar[line][-1] < prat : # original prat < new prat
        guitar[line].append(prat)   
        finger += 1     # 원래 프렛에서 손을 안뗀다
    elif guitar[line][-1] == prat : # 이전 음이랑 같은경우 
        continue
        
print(finger)
    
    

# max heapq : 33160KB, 1004ms
# for n in range(N) : 
#     line, prat = list(map(int, input().split()))
#     if guitar[line][0][1] > prat : 
#         lineLen = len(guitar[line])
#         for i in range(lineLen) : 
#             if guitar[line][0][1] > prat : 
#                 heappop(guitar[line])
#                 finger += 1     # 하나씩 손가락을 뗀다
#             elif guitar[line][0][1] == prat : 
#                 # 이미 있던 손가락이니까 유지 
#                 break
#             else :      # originalprat < prat
#                 heappush(guitar[line], (-prat, prat))
#                 finger += 1
#                 break                

#     elif guitar[line][0][1] < prat : # original prat < new prat
#         heappush(guitar[line], (-prat, prat))   # max heapq
#         finger += 1     # 원래 프렛에서 손을 안뗀다
        
#     else : # 이전 음이랑 같은경우 
#         continue
        
# print(finger)   
    