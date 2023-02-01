import sys
input = sys.stdin.readline

n = int(input())
h = list(int(input()) for _ in range(n))

stk = []
cnt = 0

for i in range(n):
    # rem le(unable to chk h[i])
    while stk and stk[-1] <= h[i]:
        stk.pop()
    stk.append(h[i])
    cnt += len(stk)-1 # xcpt self
print(cnt)