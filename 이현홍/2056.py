import sys
from collections import deque

N = int(sys.stdin.readline())
times = [0] * (N + 1)
done = [0] * (N + 1)
blocks = [0] * (N + 1)
blocks[0] = -1

worknet = {i: [] for i in range(1, N + 1)}

for idx in range(1, N + 1):
    infos = list(map(int, sys.stdin.readline().split()))
    times[idx], blocks[idx], prevs = infos[0], infos[1], infos[2:]
    for prev in prevs:
        worknet[prev].append(idx)

Q = deque()
for i in range(1, N + 1):
    if blocks[i] == 0:
        Q.append(i)
        done[i] += times[i]

while Q:
    i = Q.popleft()
    nexts = worknet[i]
    for next in nexts:
        blocks[next] -= 1
        if done[next] < done[i]:
            done[next] = done[i]
        if blocks[next] == 0:
            Q.append(next)
            done[next] += times[next]

print(max(done))
