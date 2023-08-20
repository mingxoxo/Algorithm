# 동전 1
# DP
# 23.08.19
# https://www.acmicpc.net/problem/2293

import sys
input=sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])
dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for i in range(k + 1):
        if k < coin + i:
            break
        dp[coin + i] += dp[i]

print(dp[k])
