# 2×n 타일링 2
# 24.05.10
# DP
# https://www.acmicpc.net/problem/11727


dp = [0, 1, 3]
n = int(input())
for i in range(3, n + 1):
    dp.append((dp[i - 2] * 2 + dp[i - 1]) % 10007)

print(dp[n])
