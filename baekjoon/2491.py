# 수열
# DP
# 23.09.27
# https://www.acmicpc.net/problem/2491

N = int(input())
nums = list(map(int, input().split()))
dp = [[0] * N for _ in range(2)]
dp[0][0] = dp[1][0] = 1

for i in range(1, N):
    dp[0][i] = dp[0][i - 1] + 1 if nums[i - 1] <= nums[i] else 1
    dp[1][i] = dp[1][i - 1] + 1 if nums[i - 1] >= nums[i] else 1

print(max(sum(dp, [])))
