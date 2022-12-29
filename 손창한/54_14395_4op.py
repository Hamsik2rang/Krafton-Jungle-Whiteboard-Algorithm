import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, ret):
    que = deque([(start, ret)])
    while que:
        opr, ret = que.popleft()
        # escape
        if opr == t:
            return ret
        # dict order
        for op in ('*', '+', '/'):
            if op == '*':
                tmp = opr * opr
            elif op == '+':
                tmp = opr + opr
            else:
                tmp = opr / opr
            if 0<=tmp<=t and tmp not in vis:
                vis.add(tmp)
                que.append((tmp, ret+op))
    return -1

s, t = map(int, input().split())
vis = set()
if s == t:
    print(0)
else:
    vis.add(s)
    print(bfs(s, ""))
