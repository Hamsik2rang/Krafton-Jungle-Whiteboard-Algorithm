import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

def bfs(current):
    q = deque([current])
    visited[current] = 1
    while q:
        current = q.popleft()
        if current == goal:
            return cnt[goal]
        for next in (current + up, current - down):
            if 0 < next <= total and not visited[next]:
                visited[next] = 1
                cnt[next] = cnt[current] + 1
                q.append(next)

total, current, goal, up, down = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(total + 1)]
cnt = [0 for _ in range(total + 1)]

print(bfs(current))