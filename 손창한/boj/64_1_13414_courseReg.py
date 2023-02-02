import sys
input = sys.stdin.readline

k, l = map(int, input().split())
s = dict() # s: dict(student num: waiting num)
for i in range(l): # i: waiting num
    n = input().rstrip() # n: student num
    s[n] = i # add or update waiting num
for r in sorted(s.items(), key=lambda x: x[1])[:k]:
    print(r[0])