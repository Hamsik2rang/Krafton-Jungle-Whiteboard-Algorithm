import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know = set(map(int, input().split()[1:]))
prties = []
for _ in range(m):
    prties.append(set(map(int, input().split()[1:])))

for _ in range(m):
    for prty in prties:
#        if prty.intersection(know):
#            know = know.union(prty)
        if prty & know:
            know |= prty

cnt = 0
for prty in prties:
#    if not prty.intersection(know):
    if not prty & know:
        cnt += 1
print(cnt)
