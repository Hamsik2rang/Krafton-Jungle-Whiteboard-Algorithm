import sys
inf = sys.maxsize
input = sys.stdin.readline

def dfs(i, opr):
    global pls, mns, mul, div, mx, mn
    # escape
    if i == n:
        mx = max(mx, opr)
        mn = min(mn, opr)
        return
    if pls:
        pls -= 1
        dfs(i+1, opr+a[i])
        pls += 1
    if mns:
        mns -= 1
        dfs(i+1, opr-a[i])
        mns += 1
    if mul:
        mul -= 1
        dfs(i+1, opr*a[i])
        mul += 1
    if div:
        div -= 1
        dfs(i+1, int(opr/a[i]))
        div += 1

n = int(input())
a = list(map(int, input().split()))
pls, mns, mul, div = map(int, input().split())
mx, mn = -inf, inf
dfs(1, a[0])
print(mx, mn, sep='\n')
