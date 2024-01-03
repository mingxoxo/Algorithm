# 게임을 클리어하자
# DP
# 23.01.03
# https://www.acmicpc.net/problem/28017

import sys
input=sys.stdin.readline

N, M = map(int, input().split())
time_arr = [list(map(int, input().split()))]
dp = [time_arr[0]] + [[0] * M for _ in range(N - 1)]


for i in range(1, N):
    min_time, second_min_time = sorted(dp[i - 1])[:2]
    time_arr.append(list(map(int, input().split())))

    for j in range(M):
        if min_time != dp[i - 1][j]:
            dp[i][j] = min_time + time_arr[i][j]
        else:
            dp[i][j] = second_min_time + time_arr[i][j]

print(min(dp[-1]))
