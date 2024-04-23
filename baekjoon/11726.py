# 2×n 타일링
# 24.04.23
# DP
# https://www.acmicpc.net/problem/11726


n = int(input())

dp = [0, 1, 2]

for i in range(3, n + 1):
    dp.append(dp[-2] + dp[-1])

print(dp[n] % 10007)
