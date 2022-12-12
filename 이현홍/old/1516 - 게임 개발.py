
import sys
from collections import deque

N = int(sys.stdin.readline())
build = [0] * (N + 1)

Q = deque()

for i in range(1, N + 1):
    Q.append([i] + list(map(int, sys.stdin.readline().split()[:-1])))

while Q:
    for _ in range(len(Q)):
        lst = Q.popleft()
        idx, time, prevs = lst[0], lst[1], lst[2:]
        if not prevs:
            build[idx] = time
        else:
            flag = False
            mx = 0
            for prev in prevs:
                if not build[prev]:
                    flag = True
                    break
                else:
                    mx = build[prev] if mx < build[prev] else mx
            if flag:
                Q.append(lst)
            else:
                build[idx] = mx + time


for t in build[1:]:
    print(t)
