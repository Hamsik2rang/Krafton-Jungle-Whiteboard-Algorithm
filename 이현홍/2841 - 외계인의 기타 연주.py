import sys

sys.stdin = open("input.txt", "r")

import sys

N, F = map(int, sys.stdin.readline().split())
finger = [[] for _ in range(N)]
count = 0
for _ in range(N):
    line, fret = map(int, sys.stdin.readline().split())
    while finger[line] and fret < finger[line][-1]:
        finger[line].pop()
        count += 1
    if finger[line] and fret == finger[line][-1]:
        pass
    else:
        finger[line].append(fret)
        count += 1

print(count)
