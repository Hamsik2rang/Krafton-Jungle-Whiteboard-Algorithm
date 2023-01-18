import sys
from heapq import heapify, heappush, heappop
inf = sys.maxsize
input = sys.stdin.readline

def fw():
    for i in range(1, vrtx+1):
        for u in range(1, vrtx+1):
            for v in range(1, vrtx+1):
                graph[u][v] = min(graph[u][v], graph[u][i]+graph[i][v])

vrtx = int(input())
edge = int(input())
graph = [[inf] * (vrtx+1) for _ in range(vrtx+1)]
for i in range(1, vrtx+1):
    for j in range(1, vrtx+1):
        if i == j:
            graph[i][j] = 0
for _ in range(edge):
    u, v, d = map(int, input().split())
    graph[u][v] = min(graph[u][v], d)
fw()
for i in range(1, vrtx+1):
    for j in range(1, vrtx+1):
        if graph[i][j] != inf:
            print(graph[i][j], end=" ")
        else:
            print(0, end=" ")
    print()