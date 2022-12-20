import sys
input = sys.stdin.readline

def find(node) : 
    if node != parent[node] :
        if (people[node][0] or people[parent[node]][0]) : 
            people[node][0] = people[parent[node]][0] = True 
        parent[node] = find(parent[node])
    return parent[node]

def union(x, y) :
    x = find(x)
    y = find(y)

    if x < y : 
        # 부모 갱신
        parent[y] = x 
        
        # 진실 인수 갱신 
        # 한명이라도 진실 알면 True
        if (people[x][0] or people[y][0]) : 
            people[x][0] = people[y][0] = True 
        
    else :  # x부모 > y부모
        parent[x] = y
        
        if (people[x][0] or people[y][0]) : 
            people[x][0] = people[y][0] = True 


# ppl num N / party num M
N, M = map(int, input().split())

# INITIALIZE
parent = [i for i in range(N + 1)]
parties = [False for j in range(M + 1)]
people = [[False,] for k in range(N + 1)]

tru_ppl_list = list(map(int, input().split()))

# 진실을 아는 사람 수가 0이라면 모든 파티에서 거짓말가능
if (tru_ppl_list[0] == 0) : 
    print(M)
    exit()

for _ in range(1, tru_ppl_list[0] + 1) : 
    people[tru_ppl_list[_]][0] = True
    
for m in range(1, M + 1) : 
    temp = list(map(int, input().split()))
    now_prnt = min(temp[1:])    # 이름이 제일 작은 사람 찾음
    
    for t in range(1, temp[0] + 1) : 
        people[temp[t]].append(m)
        union(now_prnt, temp[t])


for pplNum in range(1, N + 1) : 
    find(pplNum)
    if (people[pplNum][0]) and (len(people[pplNum]) > 1)  : 
        for __ in people[pplNum][1:] : 
            parties[__] = True

count = 0 
for istru in parties[1:] : 
    if not istru : 
        count += 1
print(count)


    



            
            
