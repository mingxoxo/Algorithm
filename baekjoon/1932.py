# 정수 삼각형
# DP
# 22.11.03
# https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline


def dp(N, cost):
    for i in range(N - 1, 0, -1):
        for j in range(i):
            cost[i - 1][j] += max(cost[i][j], cost[i][j + 1])
    return cost[0][0]



N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
print(dp(N, cost))
