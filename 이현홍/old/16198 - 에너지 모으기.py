import sys

sys.stdin = open("input.txt", "r")


import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


mx = -1


def DFS(s=0, n=0):
    if n == N - 2:
        global mx
        if mx < s:
            mx = s
    for i in range(1, N - 1):
        if arr[i]:
            for li in range(i - 1, -1, -1):
                if arr[li]:
                    left = arr[li]
                    break
            for ri in range(i + 1, N):
                if arr[ri]:
                    right = arr[ri]
                    break
            ori = arr[i]
            arr[i] = 0
            DFS(s + left * right, n + 1)
            arr[i] = ori


DFS()
print(mx)
