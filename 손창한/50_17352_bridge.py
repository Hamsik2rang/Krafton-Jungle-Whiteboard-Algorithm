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

n = int(input())
prnt = list(range(n+1))
for _ in range(n-2):
    x, y = map(int, input().split())
    if find(x) == find(y):
        continue
    union(x, y)

s = find(1)
for i in range(1, n+1):
    if s != find(i):
        print(s, i)
        exit()

# ret = []
# for i in range(1, n+1):
#     if i == prnt[i]:
#         ret.append(i)
# print(*ret)
