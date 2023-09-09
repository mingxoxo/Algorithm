# 돌 게임 3
# 23.09.09
# DP
# https://www.acmicpc.net/problem/9657

N = int(input())
dp = [-1] * (1001)

dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1

for i in range(5, N + 1):
    if dp[i - 1] and dp[i - 3] and dp[i - 4]:
        dp[i] = 0
    else:
        dp[i] = 1

print("SK") if dp[N] == 1 else print("CY")
