import sys
input = sys.stdin.readline
    
N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
result = set()
temp = []

def func(idx, count) : 
    if count == M : 
        result.add(tuple(temp))
        return
    count += 1 
    for i in range(idx, N) : 
        temp.append(numList[i])
        func(i + 1, count)
        temp.pop()



func(0, 0)
for i in sorted(list(result)) : 
    print(*i)
        

