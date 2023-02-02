import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    p, x = 0, 0
    for i in range(n-1, -1, -1):
        if (l[i] > x):
            x = l[i]
        else:
            p += x-l[i]
    print(p)