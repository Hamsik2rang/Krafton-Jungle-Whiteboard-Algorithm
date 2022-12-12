import sys

sys.setrecursionlimit(10**6)


def dfs(x: int, last: int, count: int):
    global check, dist
    check[x] = True

    for next in graph[x]:
        if next == last:
            continue

        if check[next]:
            dist.append(count)
            return True

        if dfs(next, x, count + 1):
            return True

    return False


n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
dist = []
for i in range(n):
    src, dest = map(int, sys.stdin.readline().split())
    graph[src].append(dest)
    graph[dest].append(src)

for i in range(n + 1):
    check = [False for _ in range(n + 1)]
    dfs(i, -1, 0)

min_dist = min(dist)
for i in range(n):
    print(dist[i] - min_dist, end=" ")
