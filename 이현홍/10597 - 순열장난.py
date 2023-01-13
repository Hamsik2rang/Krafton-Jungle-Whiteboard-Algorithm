import sys

sys.stdin = open("input.txt", "r")

import sys

numbers = sys.stdin.readline().rstrip()
L = len(numbers)
if len(numbers) < 10:
    print(*list(numbers))
    exit()

N = (L - 9) // 2 + 9
arr = []
visit = [1] * (N + 1)
visit[0] = 0


def DFS(idx=0):
    if idx == L:
        if sum(visit) == 0:
            print(*arr)
            exit()
    else:
        if idx < L - 1:
            n = int(numbers[idx : idx + 2])
            if 10 <= n <= N and visit[n]:
                arr.append(n)
                visit[n] = 0
                DFS(idx + 2)
                visit[n] = 1
                arr.pop()
        n = int(numbers[idx])
        if 0 < n < 10 and visit[n]:
            arr.append(n)
            visit[n] = 0
            DFS(idx + 1)
            visit[n] = 1
            arr.pop()

DFS()
