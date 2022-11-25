import sys

n = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a = []

for num in b:
    can3 = 0
    origin = num
    while True:
        if num % 3 == 0:
            can3 += 1
            num //= 3
        else:
            break
    a.append([can3, origin])

a.sort(key=lambda x: (-x[0], x[1]))
for i in range(n):
    print(a[i][1], end=" ")
