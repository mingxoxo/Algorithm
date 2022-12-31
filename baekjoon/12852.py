# 1로 만들기 2
# DP
# 22.12.31
# https://www.acmicpc.net/problem/12852

import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, 0] for _ in range (N + 1)] 

for idx in range(1, N):
    for next_idx in [idx * 3, idx * 2, idx + 1]:
        if next_idx <= N:
            if dp[next_idx][0] == 0 or dp[idx][0] + 1 < dp[next_idx][0]:
                dp[next_idx][0] = dp[idx][0] + 1
                dp[next_idx][1] = idx

print(dp[N][0])

idx = N
while 1 <= idx:
    print(idx, end=' ')
    idx = dp[idx][1]    
