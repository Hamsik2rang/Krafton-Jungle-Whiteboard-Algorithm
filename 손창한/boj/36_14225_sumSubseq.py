import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
sq = set()
for i in range(1, n+1):
    for j in combinations(s, i):
        sq.add(sum(j))

for k in range(1, sum(s)+2):
    if k not in sq:
        break
print(k)
