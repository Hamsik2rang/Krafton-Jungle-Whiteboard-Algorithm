import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b))
    vis[a][b] = True
    while queue:
        a, b = queue.popleft()
        c = tot - a - b
        if a == b == c:
            return 1
        for na, nb in (a, b), (a, c), (b, c):
            if na > nb:
                na -= nb
                nb += nb
            elif na < nb:
                nb -= na
                na += na
            else:
                continue
            nc = tot - na - nb
            a = min(na, nb, nc)
            b = max(na, nb, nc)
            if not vis[a][b]:
                queue.append((a, b))
                vis[a][b] = True
    return 0

a, b, c = map(int, input().split())
tot = a + b + c
vis = [[False for _ in range(tot+1)] for _ in range(tot+1)]
print(0 if tot%3 else bfs(a, b, c))
