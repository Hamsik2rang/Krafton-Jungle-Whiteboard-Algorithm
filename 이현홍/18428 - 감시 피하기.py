import sys

sys.stdin = open("input.txt", "r")

import sys

N = int(sys.stdin.readline())
dct = {"X": 0, "S": -1, "T": -2}
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def sight(r, c, k):
    if arr[r][c] == -1:
        return 1
    elif arr[r][c] == -2:
        return 0
    else:
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            n = sight(nr, nc, k)
            arr[r][c] += n
            if arr[r][c] == 2:
                two.append((r, c))
            return n
        else:
            return 0


arr = [list(map(lambda x: dct[x], list(sys.stdin.readline().rstrip().split()))) for _ in range(N)]
teachers = []
two = []
block = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == -2:
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == -1:
                        print("NO")
                        exit()
                    else:
                        block += sight(nr, nc, k)
            teachers.append((r, c))

row = [1] * N
col = [1] * N
f_two = []
for r, c in two:
    if row[r] and col[c]:
        row[r] = 0
        col[c] = 0
        f_two.append((r, c))

print("YES" if block - len(f_two) <= 3 else "NO")
