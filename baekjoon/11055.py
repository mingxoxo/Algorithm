# 가장 큰 증가하는 부분 수열
# DP
# 23.08.15
# https://www.acmicpc.net/problem/11055

n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = nums[i]
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])

print(max(dp))
