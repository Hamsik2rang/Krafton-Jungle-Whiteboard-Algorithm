# s,t <= 10**9
import sys
from collections import deque
s, t = map(int, sys.stdin.readline().strip().split())

queue = deque()
check = set()
queue.append((s,''))
check.add(s)

MAX = 10**9

if s == t:
    print(0)
else:
    res = -1
    while queue:
        c_v, c_s = queue.popleft()
        if c_v == t:
            res = c_s
            print(res)
            exit(0)

        n_v = c_v * c_v
        if 0 <= n_v <= MAX and n_v not in check:
            queue.append((n_v, c_s+'*'))
            check.add(n_v)

        n_v = c_v + c_v
        if 0 <= n_v <= MAX and n_v not in check:
            queue.append((n_v, c_s+'+'))
            check.add(n_v)

        n_v = 1
        if n_v not in check:
            queue.append((n_v, c_s+'/'))
            check.add(n_v)
    print(res)
