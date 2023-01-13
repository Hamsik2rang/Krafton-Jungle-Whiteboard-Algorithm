import sys

sys.stdin = open("input.txt", "r")

import sys

wine_count = int(sys.stdin.readline())
wine_list = [0] + [int(sys.stdin.readline()) for _ in range(wine_count)]
dp = [0 for _ in range(wine_count + 1)]

dp[1] = wine_list[1]

if wine_count > 1:
    dp[2] = wine_list[1] + wine_list[2]

    for wine in range(3, wine_count + 1):
        dp[wine] = max(dp[wine - 1], dp[wine - 3] + wine_list[wine - 1] + wine_list[wine], dp[wine - 2] + wine_list[wine])
print(dp[wine_count])
