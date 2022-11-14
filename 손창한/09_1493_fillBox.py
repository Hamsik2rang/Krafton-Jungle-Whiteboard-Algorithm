import sys
input = sys.stdin.readline

l, w, h = map(int, input().split())
n = int(input())
cl = sorted(list(list(map(int, input().split())) for _ in range(n)), reverse=True)

vol = l * w * h
ans = 0
tmp = 0
for c in cl:
    tmp *= 8
    cnt = min(c[1], l//2**c[0] * w//2**c[0] * h//2**c[0] - tmp)
    ans += cnt
    tmp += cnt
print(ans if tmp == vol else -1)
