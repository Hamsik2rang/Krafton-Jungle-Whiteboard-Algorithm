import sys

N, L, R, X = map(int, sys.stdin.readline().split())
diff = list(map(int, sys.stdin.readline().split()))
diff.sort()

count = 0
for bit in range(2**N):
    tmp = 0
    mn = 99
    mx = -1
    for i in range(N):
        code = 1 << i
        if bit & code == code:
            tmp += diff[i]
            if i < mn:
                mn = i
            if mx < i:
                mx = i
    if L <= tmp <= R and X <= diff[mx] - diff[mn]:
        count += 1

print(count)
