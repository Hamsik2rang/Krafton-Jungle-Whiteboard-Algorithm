import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
l = list(list(map(int, input().split())) for _ in range(m))
l.sort(key=lambda x: x[1])

cnt = 0
rst = [c for _ in range(n+1)]

for i in range(m):
    tmp = c
    for j in range(l[i][0], l[i][1]):
        tmp = min(tmp, rst[j])
    tmp = min(tmp, l[i][2])
    for j in range(l[i][0], l[i][1]):
        rst[j] -= tmp
    cnt += tmp
print(cnt)