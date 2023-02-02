import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

def bfs():
    queue = deque([1])
    ans = 0

    while queue:
        node = queue.popleft()

        if len(graph[node]) == 1 and node!= 1:
            ans += 1
            continue

        for next_node in graph[node]:
            if visited[next_node] == 0:
                a

iter = int(sys.stdin.readline())
graph = [[] for _ in range(iter + 1)]
visited = [0 for _ in range(iter + 1)]

for _ in range(iter - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()