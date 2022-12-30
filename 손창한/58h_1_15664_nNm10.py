import sys
input = sys.stdin.readline

def bt(dpt):
    # escape
    if len(ret) == m:
        print(*ret)
        return
    dup = 0
    for i in range(dpt, n):
        if not vis[i] and dup != arr[i]:
            vis[i] = True
            ret.append(arr[i])
            dup = arr[i]
            bt(i+1)
            vis[i] = False
            ret.pop()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # print in asc ord
vis = [False for _ in range(n)]
ret = []
bt(0)
