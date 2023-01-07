import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())
s = dict()
s[0] = 1

def dfs(i):
    if i in s:
        return s[i]
    s[i] = dfs(i//p) + dfs(i//q)
    return s[i]

print(dfs(n))