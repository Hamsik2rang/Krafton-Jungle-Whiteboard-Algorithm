import sys

t = int(sys.stdin.readline())
while t:
    t -= 1

    n = int(sys.stdin.readline())
    stock = list(map(int, sys.stdin.readline().split()))
    max_stock = [0 for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        max_stock[i] = max(max_stock[i + 1], stock[i])

    answer = 0
    for i in range(0, n):
        answer += max_stock[i] - stock[i]

    print(answer)
