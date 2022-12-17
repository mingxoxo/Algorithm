# 영재의 징검다리
# DP
# 22.12.17
# https://www.acmicpc.net/problem/24392

import sys
input = sys.stdin.readline


def dp(bridge, N, M):
    result = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if i == 0:
                result[i][j] = bridge[i][j]
                continue
            if bridge[i][j] == 0:
                continue
            if j != 0:
                result[i][j] += result[i - 1][j - 1] % 1000000007
            result[i][j] += result[i - 1][j] % 1000000007
            if j != M - 1:
                result[i][j] += result[i - 1][j + 1] % 1000000007
    print(sum(result[-1]) % 1000000007)
    


N, M = map(int, input().split())
bridge = []
for _ in range(N):
    bridge.append(list(map(int, input().split())))
dp(bridge, N, M)
