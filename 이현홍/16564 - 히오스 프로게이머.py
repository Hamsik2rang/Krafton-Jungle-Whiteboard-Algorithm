import sys

N, K = map(int, sys.stdin.readline().split())
levels = [int(sys.stdin.readline()) for _ in range(N)]
levels.sort()
levels.append(1111111111)

weight = 0
minlevel = levels[0]
for level in levels:
    if level == minlevel:
        weight += 1
    else:
        break

while K and weight <= K:
    cal = min(levels[weight] - minlevel, K // weight)
    K -= cal * weight
    minlevel += cal
    while levels[weight] == minlevel:
        weight += 1

print(minlevel)
