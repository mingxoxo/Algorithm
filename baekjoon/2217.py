# 로프
# 23.06.18
# https://www.acmicpc.net/problem/2217

import sys
input = sys.stdin.readline

N = int(input())
weight = sorted([int(input()) for i in range(N)], reverse=True)
ans = weight[0]

for i in range(1, N):
    ans = max(ans, weight[i] * (i + 1))

print(ans)
