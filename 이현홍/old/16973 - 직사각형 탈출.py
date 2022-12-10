import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [[1] + list(map(int, sys.stdin.readline().split())) + [1] for _ in range(N)]
visit = [[1] * (M + 1) for _ in range(N + 1)]
arr.insert(0, [1] * M)
arr.append([1] * M)
H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())

Q = deque()
Q.append((Sr, Sc, 1))

dir_r = [0, 0, 1, -1]
dir_c = [1, -1, 0, 0]
while Q:
    r, c, t = Q.popleft()
    for k in range(4):
        flag = True
        nr = r + dir_r[k]
        nc = c + dir_c[k]
        if 0 <= nr < N and 0 <= nc < M and visit[nr][nc]:
            visit[nr][nc] = 0
            if k <= 1:
                check_c = c - 1 if k else c + W
                for cr in range(r, r + H):
                    if arr[cr][check_c]:
                        flag = False
                        break
            else:
                check_r = r + H if k == 2 else r - 1
                for cc in range(c, c + W):
                    if arr[check_r][cc]:
                        flag = False
                        break

            if flag:
                if (nr, nc) == (Fr, Fc):
                    print(t)
                    exit()
                else:
                    Q.append((nr, nc, t + 1))

print(-1)
