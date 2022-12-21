import sys
from collections import deque

N = int(sys.stdin.readline())
edges = {i: [] for i in range(1, N + 1)}
visit = [1] * (N + 1)

for _ in range(N - 2):
    n1, n2 = sorted(map(int, sys.stdin.readline().split()))
    edges[n1].append(n2)
    edges[n2].append(n1)

Q = deque([1])
visit[1] = 0
while Q:
    node = Q.popleft()
    for next in edges[node]:
        if visit[next]:
            visit[next] = 0
            Q.append(next)
for i in range(1, N + 1):
    if visit[i]:
        print(f"1 {i}")
        exit()
