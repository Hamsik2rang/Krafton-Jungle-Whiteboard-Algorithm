import sys
input = sys.stdin.readline

n = int(input())
grph = [[] for _ in range(n+1)]
edge = [0 for _ in range(n+1)]
prnt = [0 for _ in range(n+1)]
cnt = [0 for _ in range(n+1)]
for _ in range(n):
    u, v = map(int, input().split())
    grph[u].append(v)
    edge[u] += 1
    grph[v].append(u)
    edge[v] += 1

# while node_not_in_loop
while 1 in edge:
    for i in range(1, n+1):
        # end of grph
        if edge[i] == 1:
            # save parent
            prnt[i] = grph[i][0]
            # delete end node
            edge[i] = 0
            # decrease indegree of parent
            edge[prnt[i]] -= 1
            # delete end node
            grph[prnt[i]].remove(i)

# any(): True if not all False <> all(): True if all True
while any(prnt):
    for i in range(1, n+1):
        # if grph[i] not in loop
        if prnt[i]:
            # if prnt[i] in loop
            if not prnt[prnt[i]]:
                # cnt++
                cnt[i] = cnt[prnt[i]] + 1
                # grph[i] >> in loop
                prnt[i] = 0

print(*cnt[1:])
