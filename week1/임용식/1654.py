import sys

n, k = map(int, sys.stdin.readline().split())

line = [0] * n
for i in range(n):
    line[i] = int(input())

left, right = 0, 2200000000
while left <= right:
    cut_sum = 0
    mid = (left + right) // 2
    for lan in line:
        cut_sum += lan // mid

    if cut_sum >= k:
        left = mid + 1
    else:
        right = mid - 1

print(right)
