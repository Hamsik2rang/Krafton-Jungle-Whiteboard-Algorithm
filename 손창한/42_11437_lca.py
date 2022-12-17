import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
LOG = 17

n = int(input())
grph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    grph[u].append(v)
    grph[v].append(u)
# prnt[cur][dpt] = 
prnt = [[0 for _ in range(LOG)] for _ in range(n+1)]
dpt = [0 for _ in range(n+1)]
vis = [False for _ in range(n+1)]

# cnt dpt
def dfs(x, d):
    vis[x] = True
    dpt[x] = d
    for y in grph[x]:
        if vis[y]:
            continue
        prnt[y][0] = x
        dfs(y, d+1)

# set anc
def anc():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            prnt[j][i] = prnt[prnt[j][i-1]][i-1]

# find lca
def lca(a, b):
    # dpt: a < b
    if dpt[a] > dpt[b]:
        a, b = b, a
    # set dpt same
    dif = dpt[b] - dpt[a]
    for i in range(LOG - 1, -1, -1):
        if dif >= (1<<i):
            b = prnt[b][i]
            dif -= 1<<i
    # if a is anc of b
    if a == b:
        return a
    # chk upward
    for i in range(LOG-1, -1, -1):
        if prnt[a][i] != prnt[b][i]:
            a = prnt[a][i]
            b = prnt[b][i]
    return prnt[a][0]

anc()
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
