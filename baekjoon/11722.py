# 가장 긴 감소하는 부분 수열
# DP
# 23.08.22
# https://www.acmicpc.net/problem/11722


N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[j] > nums[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
