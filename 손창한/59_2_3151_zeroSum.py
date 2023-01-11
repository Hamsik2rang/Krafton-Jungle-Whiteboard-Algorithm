import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
s = set(a)
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        x = -(a[i] + a[j])
        if x in s:
            cnt += bisect_right(a, x, j+1) - bisect_left(a, x, j+1)
print(cnt)