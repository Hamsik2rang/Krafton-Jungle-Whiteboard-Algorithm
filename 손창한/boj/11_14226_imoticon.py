import sys
from collections import deque
input = sys.stdin.readline

def bfs(emo, clp):
    queue = deque()
    queue.append((emo, clp))
    # vis[(emo, clp)] = cnt
    vis = dict()
    vis[(emo, clp)] = 0
    while queue:
        e, c = queue.popleft()
        if e == s:
            return vis[(e, c)]
        # 1. copy: screen(e), clipboard(c >> e)
        if (e, e) not in vis.keys():
            vis[(e, e)] = vis[(e, c)] + 1
            queue.append((e, e))
        # 2. paste: screen(e >> e+c), clipboard(c)
        if (e+c, c) not in vis.keys():
            vis[(e+c, c)] = vis[(e, c)] + 1
            queue.append((e+c, c))
        # 3. remove: screen(e >> e-1), clipboard(c)
        if (e-1, c) not in vis.keys():
            vis[(e-1, c)] = vis[(e, c)] + 1
            queue.append((e-1, c))

s = int(input())
print(bfs(1, 0))
