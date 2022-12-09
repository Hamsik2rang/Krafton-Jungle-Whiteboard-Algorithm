import sys
from collections import deque

# F 건물 높이 S 사람 위치 G 목적지 U 업버튼 D 다운버튼
F, S, G, U, D = map(int, sys.stdin.readline().split())

go = (U, -D)
visit = [1] * (F + 1)
visit[0] = 0
Q = deque()
Q.append((S, 0))
visit[S] = 0

while Q:
    d, t = Q.popleft()
    if d == G:
        print(t)
        exit()
    for nd in map(lambda x: x + d, go):
        if 0 < nd <= F and visit[nd]:
            visit[nd] = 0
            Q.append((nd, t + 1))

print("use the stairs")
