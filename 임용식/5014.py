import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())
check = [False for _ in range(f + 1)]
check[s] = True

q = deque()
q.append((s, 0))
while q:
    cur, count = q.popleft()

    if cur == g:
        print(count)
        exit(0)

    nu = cur + u
    if nu <= f and not check[nu]:
        q.append((nu, count + 1))
        check[nu] = True
    nd = cur - d
    if nd >= 1 and not check[nd]:
        q.append((nd, count + 1))
        check[nd] = True

print("use the stairs")
