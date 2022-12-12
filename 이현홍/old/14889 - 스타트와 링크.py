import sys
from itertools import combinations

sys.setrecursionlimit(10**5)
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

combs = tuple(combinations((i for i in range(1, N)), N // 2 - 1))

mn = 0xFFFFFFFFFFFFFF


def DFS(n=0):
    if n == len(combs):
        return
    with_zero = [0]
    without_zero = []

    for idx in range(1, N):
        if idx in combs[n]:
            with_zero.append(idx)
        else:
            without_zero.append(idx)

    team_start = sum(map(lambda x: arr[x[0]][x[1]] + arr[x[1]][x[0]], combinations(with_zero, 2)))
    team_link = sum(map(lambda x: arr[x[0]][x[1]] + arr[x[1]][x[0]], combinations(without_zero, 2)))
    diff = abs(team_start - team_link)
    global mn
    if diff < mn:
        mn = diff
        if mn == 0:
            print(0)
            exit()
    DFS(n + 1)


DFS()
print(mn)
