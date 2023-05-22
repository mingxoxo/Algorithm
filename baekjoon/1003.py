# 피보나치 함수
# DP
# 23.05.22
# https://www.acmicpc.net/problem/1003

def fibonacci(n):
    dp = [(1, 0), (0, 1)]
    for i in range(2, n + 1):
        dp.append((dp[-2][0] + dp[-1][0], dp[-2][1] + dp[-1][1]))
    return dp


T = int(input())
num = [int(input()) for _ in range(T)]
dp = fibonacci(max(num))
for i in num:
    print(*dp[i])
