import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n)]
graph = [[] for _ in range(n)]
for u in range(n):
    w, e, *v = map(int, input().split())
    dp[u] = w
    graph[u].extend(v)

for i in range(n):
    tmp = 0
    for j in graph[i]:
        tmp = max(tmp, dp[j-1])
    dp[i] += tmp
print(max(dp))
