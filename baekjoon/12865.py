# 평범한 베낭
# 22.07.28
# DP (01 Knapsack)
# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

pack = [[0] * (K + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, K + 1):
        if items[i - 1][0] > j:
            pack[i][j] = pack[i - 1][j]
        else:
            pack[i][j] = max(pack[i - 1][j], items[i - 1][1] + pack[i - 1][j - items[i - 1][0]])
        
print(pack[-1][-1])
    
