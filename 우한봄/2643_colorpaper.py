n = int(input())
p = [(1000, 1000)]
ans = 0
for _ in range(n):
    w, h = map(int, input().split())
    p.append((max(w, h), min(w, h)))

p.sort(reverse=True)

dp = [[0, p[i][1]] for i in range(n+1)]
for i in range(1, n+1):
    for j in range(i-1, -1, -1):
        if dp[j][1] >= p[i][1] and dp[j][0] + 1 > dp[i][0]:
            dp[i][0] = dp[j][0] + 1
            dp[i][1] = p[i][1]
            ans = max(ans, dp[i][0])

print(ans)