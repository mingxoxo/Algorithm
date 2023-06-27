# 퇴사
# 23.06.27
# DP
# https://www.acmicpc.net/problem/14501

import sys
input = sys.stdin.readline


N = int(input())
dp = [0] * (N + 2)
for i in range(N):
    t, p = map(int, input().split())
    dp[i + 1] = max(dp[i], dp[i + 1])
    if t + i + 1 < N + 2:
        dp[t + i + 1] = max(dp[i + 1] + p, dp[t + i + 1])

print(max(dp))
