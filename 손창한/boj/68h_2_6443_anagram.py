import sys
input = sys.stdin.readline

n = int(input())

def bt(idx):
    # escape
    if idx == len(wrd):
        print(*ret, sep='')
        return
    # back-tracking
    for i in vis:
        if vis[i]:
            vis[i] -= 1
            ret.append(i)
            bt(idx+1)
            vis[i] += 1
            ret.pop()

for _ in range(n):
    wrd = sorted(list(input().rstrip()))
    vis = dict()
    ret = list()
    # set visited_arr
    for c in wrd:
        if c in vis:
            vis[c] += 1
        else:
            vis[c] = 1
    # back-tracking
    bt(0)