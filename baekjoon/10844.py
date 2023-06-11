# 쉬운 계단 수
# 23.06.11
# DP
# https://www.acmicpc.net/problem/10844

#1
N = int(input())
dp = [[0] * 10 for _ in range(N + 1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1] % 1000000000
    dp[i][9] = dp[i - 1][8] % 1000000000
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] % 1000000000 + dp[i - 1][j + 1] % 1000000000

print(sum(dp[N]) % 1000000000)


#2 
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 12 for _ in range(N)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
mod = 10 ** 9

for i in range(1, N):
    for j in range(10):
        dp[i][j] = dp[i - 1][j - 1] % mod + dp[i - 1][j + 1] % mod

print(sum(dp[-1]) % mod)
