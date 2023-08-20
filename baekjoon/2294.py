# 동전 2
# DP
# 23.08.20
# https://www.acmicpc.net/problem/2294

import sys
input=sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])
dp = [10**6] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(k + 1):
        if k < coin + i:
            break
        dp[coin + i] = min(dp[i] + 1, dp[coin + i])

print(dp[k]) if dp[k] != 10**6 else print(-1)
