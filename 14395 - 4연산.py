import sys
from collections import deque

start, end = map(int, sys.stdin.readline().split())

if start == end:
    print(0)
    exit()

visit = {start: ""}
Q = deque([start])

while Q:
    n = Q.popleft()
    if n == end:
        print(visit[n])
        exit()

    for next, opr in ((n**2, "*"), (n + n, "+"), (0, "-"), (1, "/")):
        if visit.get(next, -1) == -1 and next <= end:
            visit[next] = visit[n] + opr
            Q.append(next)

print(-1)
