import sys
from heapq import heapify, heappush, heappop
inf = sys.maxsize
input = sys.stdin.readline

# dijkstra with priority queue(heap), O((V+E)logV)
def dijkstra(start):
    heap = []
    heappush(heap, (start, 0))
    dis[start] = 0
    while heap:
        node, tmp = heappop(heap)
        if dis[node] < tmp:
            continue
        for next in graph[node]:
            dist = dis[node] + next[1]
            if dist < dis[next[0]]:
                dis[next[0]] = dist
                heappush(heap, (next[0], dist))

vrtx, edge = map(int, input().split())
start = int(input())
graph = [[] for _ in range(vrtx+1)]
for _ in range(edge):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
dis = [inf] * (vrtx+1)

dijkstra(start)
for d in dis[1:]:
    print("INF" if d == inf else d)