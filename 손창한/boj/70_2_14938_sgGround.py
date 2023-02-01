import sys
from heapq import heapify, heappush, heappop
inf = sys.maxsize
input = sys.stdin.readline

n, m, r = map(int, input().split())
t = list(map(int, input().split()))
g = [[inf] * (n+1) for _ in range(n+1)]

# set graph(bi-direction)
for i in range(1, n+1):
    g[i][i] = 0
for i in range(r):
    u, v, d = map(int, input().split())
    g[u][v] = min(g[u][v], d)
    g[v][u] = min(g[v][u], d)
# floyd-warshall
for i in range(1, n+1):
    for u in range(1, n+1):
        for v in range(1, n+1):
            g[u][v] = min(g[u][v], g[u][i]+g[i][v])
# count max items
cnt = 0
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if g[i][j] <= m:
            tmp += t[j-1]
    cnt = max(cnt, tmp)
print(cnt)