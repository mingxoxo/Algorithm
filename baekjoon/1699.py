# 제곱수의 합
# DP
# 23.09.17
# https://www.acmicpc.net/problem/1699
# 시간초과 해결 참고: https://www.acmicpc.net/board/view/116375

N = int(input())
dp = [10 ** 6] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[N])
