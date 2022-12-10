import sys

N = int(sys.stdin.readline())

spend = []
earn = []

for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    spend.append(t)
    earn.append(p)


mx = -1


def DFS(s=0, idx=0):
    if idx == N:
        global mx
        if mx < s:
            mx = s
    elif N < idx:
        return
    else:
        DFS(s + earn[idx], idx + spend[idx])
        DFS(s, idx + 1)


DFS()
print(mx)
