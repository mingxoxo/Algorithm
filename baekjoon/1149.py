# RGB거리
# DP
# 22.11.03
# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline


def dp(N, cost):
    for i in range(1, N):
        cost[i][0] += min(cost[i - 1][1], cost[i - 1][2])
        cost[i][1] += min(cost[i - 1][0], cost[i - 1][2])
        cost[i][2] += min(cost[i - 1][0], cost[i - 1][1])
    return min(cost[N-1])



N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
print(dp(N, cost))
