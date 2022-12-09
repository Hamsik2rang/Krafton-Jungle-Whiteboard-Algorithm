import sys
input = sys.stdin.readline
from collections import deque
# sys.setrecursionlimit(10**6)

A, B, C = map(int, input().split())
nSum = A + B + C
visited = [[0 for i in range(nSum + 1)] for j in range(nSum + 1)] 
queue = deque()

def bfs() : 
    queue.append([A, B])
    visited[A][B] = 1
    
    while queue : 
        X, Y = queue.popleft()
        Z = nSum - X - Y
        
        if X == Y == Z : 
            return 1
        
        for m, n in (X, Y), (Y, Z), (X, Z) : 
            if (m == n) : 
                continue
            elif (m < n) : 
                n -= m
                m = 2 * m
            else : 
                m -= n
                n = 2 * n
            l = nSum - m - n
            
            X = min(m, n, l)
            Y = max(m, n, l)
            
            if visited[X][Y] == 0 : 
                queue.append([X, Y])
                visited[X][Y] = 1
                
    return 0
            

if (nSum % 3) : 
    print(0)
else : 
    print(bfs())            
                    


# +++++++++++++++++++++++++++++BFS 시간초과+++++++++++++++++++++++++++++++
# def bfs() : 
#     queue.append(sorted([A, B, C]))
#     visited.append(sorted([A, B, C]))
    
#     while queue : 
#         nowList = queue.popleft()
#         visited.append(nowList)
#         nA = nowList[0]
#         nB = nowList[1]
#         nC = nowList[2]
        
#         if nA == nB == nC : 
#             return 1
#         nSum = nA + nB + nC
#         for i in range(3) : 
#             for j in range(3) : 
#                 if nowList[i] < nowList[j] : 
#                     X = nowList[i]
#                     Y = nowList[j]
#                     new = sorted([2*X, Y - X, nSum - X - Y])
#                     if new not in visited : 
#                         queue.append(new)
#                         visited.append(new)
#     return 0
                  




# ++++++++++++++++++++++++ DFS ++++++++++++++++++++++++++++++
# def dfs(newList) : # 시간초과
#     if newList not in visited : 
#         A = newList[0]
#         B = newList[1]
#         C = newList[2]
#         visited.append(newList)
        
#         if A == B == C : return 1
        
#         # Case 1 A, B
#         flag1 = dfs(sorted([B - A, A + A, C]))
#         # Case 2 A, C
#         flag2 = dfs(sorted([C - A, A + A, B]))
#         # Case 3 B, C
#         flag3 = dfs(sorted([C - B, B + B, A]))
#         if flag1 or flag2 or flag3 : 
#             return 1
#         else : return 0
#     else : 
#         return 0

# 과정을 거치다가 무한루프 나면 불가능 
# 계산 과정상 음수나 0이 나올 수 없다 

# 3으로 안나눠지면 불가능 
# even-even-odd 불가능!
# odd-odd-odd 이라면 처음부터 3개가 같은 경우가 아니라면 불가능 

# if (nSum % 3) : 
    # print(0)
# elif (A % 2) and (B % 2) and (C % 2) : # odd-odd-odd
#     if (A == B == C) : 
#         print(0)
#     else : 
#         print(-1)
# else : 
    # thisList = sorted([A, B, C])
    # print(dfs(thisList))  
    

