import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    ret = [0] * (n+1)
    queue = deque()
    for i in range(1, n+1):
        if indgr[i] == 0:
            queue.append(i)
    while queue:
        j = queue.popleft()
        ret[j] += spend[j]
        for k in graph[j]:
            ret[k] = max(ret[k], ret[j])
            indgr[k] -= 1
            if indgr[k] == 0:
                queue.append(k)
    return ret[1:]

n = int(input())
indgr = [0] * (n+1)
spend = [0] * (n+1)
graph =[[] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    spend[i] = tmp[0]
    for j in tmp[1:-1]:
        graph[j].append(i)
        indgr[i] += 1
print(*topology_sort(), sep="\n")
