import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

turn = 0
root = 1
N = int(sys.stdin.readline())
parent = {e: [] for e in range(1, N + 1)}
visit = [0] * (N + 1)
visit[0] = 1

for _ in range(N - 1):
    e1, e2 = map(int, sys.stdin.readline().split())
    visit[e1] += 1
    visit[e2] += 1
    parent[e1].append(e2)
    parent[e2].append(e1)


childs = []
for idx in range(1, N + 1):
    if visit[idx] == 1:
        childs.append(idx)

moves = [0] * (N + 1)
Q = deque([1])
while Q:
    node = Q.popleft()
    visit[node] = 0
    edges = parent[node]
    for e in edges:
        if visit[e]:
            moves[e] = moves[node] + 1
            Q.append(e)

print("Yes" if sum(map(lambda x: moves[x], childs)) % 2 else "No")
