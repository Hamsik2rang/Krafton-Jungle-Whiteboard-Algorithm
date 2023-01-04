import sys
input = sys.stdin.readline

def isPal(s, e):
    m = (s+e)//2
    pal = []
    for i in range(s-1, e):
        if i <= m: # left
            if i == m and (e-s)%2: # mid
                continue
            pal.append(a[i])
        else: # right
            if a[i] != pal.pop():
                return 0
    return 1

n = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(isPal(s-1, e-1))