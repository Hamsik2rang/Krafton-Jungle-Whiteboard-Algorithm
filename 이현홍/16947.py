import sys

def move(prev, now):
    info[now] = 1
    for next in edges[now]:
        if prev != next:
            linked[next] -= 1
            if linked[next] == 1:
                move(now, next)
            elif linked[next] == 2:
                circles.append(next)

def move2(prev, now, d):
    distance[now] = d
    visited[now] = 0
    for next in edges[now]:
        if prev != next and visited[next] and info[next]:
            move2(now, next, d + 1)


N = int(sys.stdin.readline())
edges = {i: [] for i in range(1, N + 1)}
linked = [0] * (N + 1)
for _ in range(N):
    stn1, stn2 = map(int, sys.stdin.readline().split())
    edges[stn1].append(stn2)
    edges[stn2].append(stn1)
    linked[stn1] += 1
    linked[stn2] += 1

ends = []
for idx in range(1, N + 1):
    if linked[idx] == 1:
        ends.append(idx)

circles = []
info = [0] * (N + 1)
for end in ends:
    move(-1, end)

distance = [0] * (N + 1)
visited = [1] * (N + 1)
for c in circles:
    if not info[c]:
        move2(-1, c, 0)

print(*distance[1:])
