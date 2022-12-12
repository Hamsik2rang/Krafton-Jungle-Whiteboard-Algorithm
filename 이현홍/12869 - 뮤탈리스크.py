import sys
from collections import deque

N = int(sys.stdin.readline())
targets = list(sorted(list(map(int, sys.stdin.readline().split()))))
for _ in range(3 - N):
    targets.append(0)

visit = [[[0xFFFF] * 61 for _ in range(61)] for __ in range(61)]


def hit(now):
    a, b, c = now
    return ((a - 9, b - 3, c - 1), (a - 9, b - 1, c - 3), (a - 3, b - 9, c - 1), (a - 3, b - 1, c - 9), (a - 1, b - 3, c - 9), (a - 1, b - 9, c - 3))


Q = deque()
Q.append(targets)
visit[targets[0]][targets[1]][targets[2]] = 0


while Q:
    now = Q.pop()
    for new in hit(now):
        nt1, nt2, nt3 = new
        nt1 = 0 if nt1 < 0 else nt1
        nt2 = 0 if nt2 < 0 else nt2
        nt3 = 0 if nt3 < 0 else nt3
        new = (nt1, nt2, nt3)
        if visit[now[0]][now[1]][now[2]] + 1 < visit[nt1][nt2][nt3]:
            visit[nt1][nt2][nt3] = visit[now[0]][now[1]][now[2]] + 1
            Q.append(new)

print(visit[0][0][0])
