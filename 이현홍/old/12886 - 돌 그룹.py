import sys
from collections import deque

A, B, C = sorted(list(map(int, sys.stdin.readline().split())))
if (A + B + C) % 3:
    print(0)
    exit()
elif A == B == C:
    print(1)
    exit()

visit = [[1] * 501 for _ in range(501)]
Q = deque()
Q.append([A, B, C])

while Q:
    a, b, c = Q.popleft()
    for (na, nb, nc) in (sorted([a + a, b, c - a]), sorted([a + a, b - a, c]), sorted([a, b + b, c - b])):
        if not (0 <= nc - nb < 500 and 0 <= nb - na < 500):
            continue
        if na == nb == nc:
            print(1)
            exit()
        elif visit[nc - nb][nb - na]:
            visit[nc - nb][nb - na] = 0
            Q.append((na, nb, nc))

print(0)
