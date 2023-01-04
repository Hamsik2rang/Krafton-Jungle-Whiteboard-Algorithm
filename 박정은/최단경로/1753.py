from collections import deque


def bfs(start):
    queue = deque()

    for i in lst[start]:
        queue.append(i)

    cost_list[start] = 0

    while queue:
        cost, dst, befo = queue.popleft()

        ssum = cost_list[befo] + cost

        if cost_list[dst] > ssum and not visited[dst]:
            cost_list[dst] = ssum
            visited[dst] = True
            for i in lst[dst]:
                queue.append(i)


V, E = map(int, input().split())

st = int(input())
INF = int(10e9)
cost_list = [INF] * (V + 1)
lst = [[] for _ in range(E+1)]
visited = [False for _ in range(E+1)]

for _ in range(E):
    s, d, c = map(int, input().split())
    lst[s].append((c, d, s))

bfs(st)

for one in cost_list[1:]:

    if one == INF:
        print('INF')
    else:
        print(one)
