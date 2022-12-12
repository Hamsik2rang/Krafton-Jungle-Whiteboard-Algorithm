import sys
from collections import deque

N = int(sys.stdin.readline())
Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())
D = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
V = [[1] * N for _ in range(N)]
Q = deque()
Q.append((Sr, Sc, 0))
V[Sr][Sc] = 0
while Q:
    r, c, t = Q.popleft()
    new = tuple(map(lambda x: (r + x[0], c + x[1], t + 1), D))
    for (nr, nc, t) in new:
        if 0 <= nr < N and 0 <= nc < N and V[nr][nc]:
            if (nr, nc) == (Fr, Fc):
                print(t)
                exit()
            V[nr][nc] = 0
            Q.append((nr, nc, t))
print(-1)
