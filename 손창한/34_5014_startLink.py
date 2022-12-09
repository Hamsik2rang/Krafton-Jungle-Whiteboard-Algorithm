import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    queue = deque([s])
    vis[s] = True
    while queue:
        i = queue.popleft()
        # escape
        if i == g:
            return cnt[g]
        for j in [i+u, i-d]:
            if 0<j<=f and not vis[j]:
                vis[j] = True
                cnt[j] = cnt[i]+1
                queue.append(j)
    # fail
    return "use the stairs"

f, s, g, u, d = map(int, input().split())
vis = [False for _ in range(f+1)]
cnt = [0 for _ in range(f+1)]
print(bfs(s))
