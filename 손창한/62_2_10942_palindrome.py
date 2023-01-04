import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [[False for _ in range(n)] for _ in range(n)]
for cnt in range(n):
    for s in range(n - cnt):
        e = s + cnt
        if s == e:
            # cnt == 0
            dp[s][e] = True
        elif a[s] == a[e]:
            # isPal btwn next(fin) or each sides
            if s+1 == e or dp[s+1][e-1]:
                dp[s][e] = True

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(1 if dp[s-1][e-1] else 0)