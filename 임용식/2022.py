import sys

x, y, c = map(float, sys.stdin.readline().split())

high = min(x, y)
low = 1
answer = 0
epsilon = 1e-6

while epsilon <= high - low:
    mid = (low + high) / 2

    left_height = (x**2 - mid**2) ** 0.5
    right_height = (y**2 - mid**2) ** 0.5
    candidate = (left_height * right_height) / (left_height + right_height)

    if candidate >= c:
        answer = mid
        low = mid
    else:
        high = mid

print(answer)
