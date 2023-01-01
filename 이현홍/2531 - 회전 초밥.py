import sys

sys.stdin = open("input.txt", "r")

import sys

N, d, k, c = map(int, sys.stdin.readline().split())
sushi = list(map(int, sys.stdin.readlines()))
sushi += sushi[:k]

mx = 0
for i in range(N):
    mx = max(mx, len(set(sushi[i : i + k]) | set([c])))
print(mx)
