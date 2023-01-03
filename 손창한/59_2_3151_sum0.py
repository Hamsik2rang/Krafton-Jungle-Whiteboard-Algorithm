import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
idx = list(range(n))
cnt = 0

for c in combinations(idx, 3):
    if sum([arr[x] for x in c]) == 0:
        cnt += 1
print(cnt)