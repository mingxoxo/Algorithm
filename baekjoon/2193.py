# 이친수
# 23.03.09
# DP
# https://www.acmicpc.net/problem/2193

N = int(input())

if N < 3:
    print(1)
else:
    dp = [1, 1]
    for _ in range(4, N + 1):
        dp = [dp[0] +dp[1], dp[0]]
    print(sum(dp))
    
