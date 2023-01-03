import sys

sys.stdin = open("input.txt", "r")

import sys
from heapq import heappush, heappop

def dijkstra(start):
    heap = []
    distances[start] = 0  # 시작 값은 0이어야 함
    heappush(heap, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while heap:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heappop(heap)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        
        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heappush(heap, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return distances

node, edge = map(int, sys.stdin.readline().split())
start_node = int(sys.stdin.readline())
graph = [[] for _ in range (node + 1)]
distances = [100_000_000] * (node + 1)

for _ in range(edge):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append([end, weight])

dijkstra(start_node)
for distance in distances[1:]:
    if distance != 100_000_000:
        print(distance)
    else:
        print('INF')
