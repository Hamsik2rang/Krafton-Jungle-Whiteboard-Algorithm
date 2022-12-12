import sys
from itertools import combinations

n = int(sys.stdin.readline())
check = [False for _ in range(2_000_001)]
lst = list(map(int, sys.stdin.readline().split()))

for i in range(1, n + 1):
    for comb in combinations(lst, i):
        sum = 0
        for num in comb:
            sum += num
        check[sum] = True

min_num = min(lst)
for i in range(1, 2_000_001):
    if not check[i]:
        print(i)
        break
