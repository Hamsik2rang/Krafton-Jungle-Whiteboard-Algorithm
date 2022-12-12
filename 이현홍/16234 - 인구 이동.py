import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def grouping(r, c, num):
    Q = deque([(r, c)])
    groups[r][c] = num
    total = arr[r][c]
    cnt = 1
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and L <= abs(arr[nr][nc] - arr[r][c]) <= R and groups[nr][nc] < groups[r][c]:
                groups[nr][nc] = num
                Q.append((nr, nc))
                total += arr[nr][nc]
                cnt += 1
    return total // cnt


flag = True
days = 0
changes = []
groups = [[0] * N for _ in range(N)]
populations = [0]
group_num = 0
while flag:
    flag = False
    if changes:
        for change in changes:
            r, c = change
            group_num += 1
            populations.append(grouping(r, c, group_num))
    else:
        for r in range(N):
            for c in range(N):
                if not groups[r][c]:
                    group_num += 1
                    populations.append(grouping(r, c, group_num))
    tmp = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] != populations[groups[r][c]]:
                tmp.append((r, c))
                arr[r][c] = populations[groups[r][c]]
    if tmp:
        changes = tmp
        flag = True
        days += 1

print(days)
