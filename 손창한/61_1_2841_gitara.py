import sys
input = sys.stdin.readline

n, p = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))

cnt = 0
stk = [[0] for _ in range(7)]
for l, f in a:
    while stk[l]:
        if stk[l][-1] > f:
            stk[l].pop()
            cnt += 1
        else:
            break
    if stk[l][-1] == f:
        continue
    stk[l].append(f)
    cnt += 1
print(cnt)