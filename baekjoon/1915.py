# 가장 큰 정사각형 -- BSQ !
# DP
# 22.09.28
# https://www.acmicpc.net/problem/1915

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            continue
        if i != 0 and j != 0:
            arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + arr[i][j]
        if result < arr[i][j]:
            result = arr[i][j]
            
print(result**2)
