import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
grf = defaultdict(list)
vis = {i: False for i in range(1, n+1)}
for _ in range(n-1):
    u, v = map(int, input().split())
    grf[u].append(v)
    grf[v].append(u)

def bfs(node):
    que = deque()
    que.append([node, 0])
    vis[node] = True
    cnt = 0
    while que:
        cur, dpt = que.popleft()
        for nxt in grf[cur]:
            if not vis[nxt]:
                vis[nxt] = True
                que.append([nxt, dpt+1])
                if len(grf[nxt]) == 1:
                    cnt += dpt+1
    return cnt

print("Yes" if bfs(1)%2 else "No")