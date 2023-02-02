import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(u, wu):
    for v, wv in graph[u]:
        if vis[v] == -1:
            vis[v] = wu+wv
            dfs(v, wu+wv)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, w = map(int, input().split())
    graph[x].append([y, w])
    graph[y].append([x, w])
# find farthest one from root
vis = [-1 for _ in range(n+1)]
vis[1] = 0
dfs(1, 0)

# find farthest another from the one above
s = vis.index(max(vis))
vis = [-1 for _ in range(n+1)]
vis[s] = 0
dfs(s, 0)

print(max(vis))
