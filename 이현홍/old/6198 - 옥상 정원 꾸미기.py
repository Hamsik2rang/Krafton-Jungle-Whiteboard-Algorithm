import sys

sys.stdin = open("input.txt", "r")
import sys

N = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readlines()))[::-1]
heights.append(1000000001)
heights.insert(0, 1000000001)

benchs = [0] * (N + 1)
stack = []
for idx in range(N + 1):
    while stack and heights[idx] > stack[-1][0]:
        h, i = stack.pop()
        benchs[idx] += 1 + benchs[i]
    stack.append((heights[idx], idx))

print(sum(benchs))
