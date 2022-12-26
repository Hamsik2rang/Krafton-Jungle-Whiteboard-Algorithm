import sys
input = sys.stdin.readline

R, C = map(int, input().split())
lst = [input().strip() for _ in range(R)]

ans = 1
for s in lst:
    if s.count('SW') or s.count('WS'):
        ans = 0
        break

for s in map(lambda x: ''.join(x), zip(*lst)):
    if s.count('SW') or s.count('WS'):
        ans = 0
        break

print(ans)
if ans:
    for s in lst:
        print(s.replace('.', 'D'))