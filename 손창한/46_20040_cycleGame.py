import sys
input = sys.stdin.readline

def find(x):
    if x != prnt[x]:
        prnt[x] = find(prnt[x])
    return prnt[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        prnt[y] = x
    else:
        prnt[x] = y

n, m = map(int, input().split())
prnt = list(range(n)) # [i for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    # cycle made
    if find(x) == find(y):
        print(i+1)
        exit()
    union(x, y)
# no cycle
print(0)
