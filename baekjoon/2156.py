# 포도주 시식
# 23.06.10
# DP
# https://www.acmicpc.net/problem/2156

import sys
input = sys.stdin.readline

n = int(input())
cup = [int(input()) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0][1] = cup[0]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + cup[i]
    dp[i][2] = dp[i - 1][1] + cup[i]

print(max(dp[n - 1]))
