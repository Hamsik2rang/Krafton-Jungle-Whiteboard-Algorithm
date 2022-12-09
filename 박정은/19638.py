import heapq

N,H,T= map(int,input().split())

q = []
flag = True
for i in range(N):
    heapq.heappush(q, -(int(input())))



while T:
    comp = -heapq.heappop(q)
    if comp >= H:
        heapq.heappush(q, -(comp>>1))
        T -= 1
    else:
        break
else:
    comp = -heapq.heappop(q)
    flag = False
    if comp > H:
        print('YES')
        print(comp)
    else:
        print('NO')
        print(comp)

if flag:
    print('YES')
    print(comp)
