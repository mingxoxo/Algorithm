# 가장 긴 증가하는 부분 수열
# 22.07.26
# DP
# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, len(A)):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))



