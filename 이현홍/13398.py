import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

if max(nums) <= 0:  # 양수가 하나도 없을 경우 가장 큰 값 하나를 출력하고 종료
    print(max(nums))
    exit()


L = len(nums)
dp = [[0, 0] for _ in range(L + 1)]

mx = -1
for idx in range(1, L + 1):
    dp[idx][0] = max(dp[idx - 1][0] + nums[idx - 1], nums[idx - 1])  # 앞 수들의 합이 음수면 끊음
    dp[idx][1] = max(dp[idx - 1][0], dp[idx - 1][1] + nums[idx - 1])  # 숫자 하나를 이미 뺀 경우와 새로 빼는 경우를 비교


for idx in range(1, L + 1):
    for j in range(2):
        if mx < dp[idx][j]:
            mx = dp[idx][j]

print(mx)
