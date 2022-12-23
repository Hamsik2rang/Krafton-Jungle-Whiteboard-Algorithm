import sys
from collections import deque

N = int(sys.stdin.readline())
edges = {i: [] for i in range(1, N + 1)}
visit = [1] * (N + 1)
visit[0] = 0
for _ in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    edges[n1].append(n2)
    edges[n2].append(n1)

routes = [""] * (N + 1)
Q = deque()
Q.append(1)
visit[1] = 0
routes[1] = "0"

while Q:
    idx = Q.popleft()
    d = 0
    for node in edges[idx]:
        if visit[node]:
            visit[node] = 0
            Q.append(node)
            routes[node] = routes[idx] + str(d)
            d += 1

M = int(sys.stdin.readline())
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    s1, s2 = routes[n1], routes[n2]
    l1, l2 = len(s1), len(s2)
    compare = ""
    for i in range(min(l1, l2)):
        if s1[i] == s2[i]:
            compare += s1[i]
        else:
            break
    print(routes.index(compare))
