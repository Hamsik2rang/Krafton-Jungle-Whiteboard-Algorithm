import sys
from collections import deque
input = sys.stdin.readline

def bfs(chk, cnt):
    (r1, c1), (r2, c2) = chk
    queue = deque()
    queue.append((r1, c1, r2, c2, cnt))
    while queue:
        r1, c1, r2, c2, cnt = queue.popleft()
        # escape
        if cnt >= 10:
            break
        for i in range(4):
            nr1, nc1 = r1+dr[i], c1+dc[i]
            nr2, nc2 = r2+dr[i], c2+dc[i]
            fw1, fw2 = False, False
            # drop 2
            if not (-1<nr1<n and -1<nc1<m) and not (-1<nr2<n and -1<nc2<m):
                continue
            # drop 1
            if not (-1<nr1<n and -1<nc1<m) or not (-1<nr2<n and -1<nc2<m):
                return cnt+1
            # drop 0
            if brd[nr1][nc1] == '#':
                nr1, nc1 = r1, c1
                fw1 = True
            if brd[nr2][nc2] == '#':
                nr2, nc2 = r2, c2
                fw2 = True
            if not (fw1 and fw2):
                queue.append((nr1, nc1, nr2, nc2, cnt+1))
    return -1

n, m = map(int, input().split())
brd, chk = [], []
for i in range(n):
    l = input().rstrip()
    for j in range(m):
        if l[j] == "o":
            chk.append((i, j))
    brd.append(list(l))
vis = [[0 for _ in range(m)] for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1 ,0]
print(bfs(chk, 0))
