import sys
from collections import deque

s = int(sys.stdin.readline())
check = dict()
check[(1, 0)] = 0
q = deque()
q.append((1, 0))

while len(q) > 0:
    cur, clipboard = q.popleft()

    if cur == s:
        print(check[(cur, clipboard)])
        break

    if (cur, cur) not in check.keys():
        check[(cur, cur)] = check[(cur, clipboard)] + 1
        q.append((cur, cur))

    if (cur - 1, clipboard) not in check.keys():
        check[(cur - 1, clipboard)] = check[(cur, clipboard)] + 1
        q.append((cur - 1, clipboard))

    if (cur + clipboard, clipboard) not in check.keys():
        check[(cur + clipboard, clipboard)] = check[(cur, clipboard)] + 1
        q.append((cur + clipboard, clipboard))
