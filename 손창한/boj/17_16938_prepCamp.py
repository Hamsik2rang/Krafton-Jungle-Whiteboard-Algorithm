import sys
from itertools import combinations
input = sys.stdin.readline

n, l, r, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

cnt = 0
for i in range(2, n+1):
    for j in combinations(a, i):
        if l <= sum(j) <= r and max(j)-min(j) >= x:
            cnt += 1
print(cnt)
