import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

visit = [float("INF")] * (V + 1)
edges = {i: {} for i in range(1, V + 1)}
for iter in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if edges[u].get(v, 0):
        edges[u][v] = min(edges[u][v], w)
    else:
        edges[u][v] = w

Q = deque([(start, 0)])
while Q:
    n, w = Q.popleft()
    for key in edges[n].keys():
        if edges[n][key] + w < visit[key]:
            visit[key] = edges[n][key] + w
            Q.append((key, edges[n][key] + w))

visit[start] = 0
for one in visit[1:]:
    print("INF") if one == float("INF") else print(one)
