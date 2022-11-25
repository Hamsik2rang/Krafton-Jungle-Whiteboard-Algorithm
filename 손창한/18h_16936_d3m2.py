import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))
a = []

for i in b:
    cnt = 0
    tmp = i
    while True:
        if tmp % 3 == 0:
            cnt += 1
            tmp //= 3
        else:
            break
    a.append([cnt, i])
# sort by (div3 cnt, num size)
a.sort(key=lambda x: (-x[0], x[1]))
for i in range(n):
    print(a[i][1], end=" ")
