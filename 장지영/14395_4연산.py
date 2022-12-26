import sys
input = sys.stdin.readline
from collections import deque

visited = set({})
q = deque()

def bfs(T, S) : 
    q.append([S, ''])
    
    while q : 
        nowSList = q.popleft()
        nowS = nowSList[0]
        math = nowSList[1]
        
        visited.add(nowS)
        
        if nowS == T : 
            return math
        
        for i in range(3) : 
            if (i == 0) : 
                newS = nowS * nowS
                newMath = math + '*'
                if (newS not in visited) and (newS <= 1000_000_000) : 
                    q.append([newS, newMath])
                    visited.add(newS)
            elif (i == 1) : 
                newS = nowS + nowS
                newMath = math + '+'  
                if (newS not in visited) and (newS <= 1000_000_000) : 
                    q.append([newS, newMath])   
                    visited.add(newS)
            else : 
                newS = 1
                newMath = math + '/'
                if (newS not in visited) and (1 <= newS <= 1000_000_000) : 
                    q.append([newS, newMath])   
                    visited.add(newS)
                
                
    print(-1)
    exit() 


# 가지치기
# 1. T가 S의 배수일때 
# 2. T가 S의 배수는 아니지만 2의 배수일 때 
# 두 경우 말고는 -1
S, T = map(int, input().split())
if S == T : 
    print(0)
    exit()
elif T == 0 : 
    print('-')
    exit()
elif (T % S != 0) and (T % 2 != 0) : 
    if T == 1 : 
        print('/')
        exit()
    else : 
        print(-1)
        exit()
else : 
    print(bfs(T, S))