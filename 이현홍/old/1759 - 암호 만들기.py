import sys

sys.stdin = open("input.txt", "r")

import sys
from itertools import combinations

L, C = map(int, input().split())
alp = set(input().split())
m = alp & {"a", "e", "i", "o", "u"}
s = alp - {"a", "e", "i", "o", "u"}
result = []
for i in range(1, L - 1):
    ms = tuple(combinations(m, i))
    ss = tuple(combinations(s, L - i))
    for one in ms:
        for two in ss:
            result.append("".join(sorted([*one, *two])))

for one in sorted(result):
    print(one)
