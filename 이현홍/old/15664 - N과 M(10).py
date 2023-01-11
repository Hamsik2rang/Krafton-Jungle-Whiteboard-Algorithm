import sys

sys.stdin = open("input.txt", "r")

from itertools import combinations

_, M = map(int, input().split())
[print(*x) for x in sorted(set(combinations(sorted((map(int, input().split()))), M)))]
