# 카드 구매하기
# DP
# 23.04.13
# https://www.acmicpc.net/problem/11052

N = int(input())
money = list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(0, N + 1):
    for j in range(1, N - i + 1):
        dp[i + j] = max(dp[i + j], dp[i] + money[j - 1])
    
print(dp[-1])
