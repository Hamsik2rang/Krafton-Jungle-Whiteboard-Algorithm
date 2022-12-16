import sys
input = sys.stdin.readline
from queue import deque

# Char number N, risable lv sum K
N, K = map(int, input().split())

tempList = []
for _ in range(N) : 
    tempList.append(int(input()))
    
charList = deque(sorted(tempList))

while K : 
    minList = []
    minList.append(charList.popleft())
    while minList[0] == charList[0] : 
        minList.append(charList.popleft())
    
    diff = charList[0] - minList[0]     # charList 다음 작은 원소와의 차이 
    howMany = len(minList)
    if diff * howMany > K : 
        minList[0] += K // howMany
        print(minList[0])
        exit()
    else :      # diff * howMany < K
        minList = list(map(lambda x : x + diff, minList))
        K -= diff * howMany
        for m in range(howMany) : 
            charList.appendleft(minList[m])

        
    
        
