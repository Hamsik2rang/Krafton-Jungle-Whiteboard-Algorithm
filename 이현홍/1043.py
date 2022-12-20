import sys

N, M = map(int, sys.stdin.readline().split())
T, *watchdogs = map(int, sys.stdin.readline().split())

watchdogs = set(watchdogs)
parties = []
visit = [1] * M
for _ in range(M):
    n, *members = map(int, sys.stdin.readline().split())
    parties.append(set(members))

flag = 1
while flag:
    flag = 0

    for idx, party in enumerate(parties):
        if watchdogs & party and visit[idx]:
            flag = 1
            visit[idx] = 0
            watchdogs = watchdogs | party

print(sum(visit))
