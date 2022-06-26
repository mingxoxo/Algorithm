# 행렬 덧셈
# https://www.acmicpc.net/problem/2738

import sys
input = sys.stdin.readline

A = []
B = []
result = []

N, M = map(int, input().split())

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    result.append([A[i][j] + B[i][j] for j in range(M)])

for i in range(N):
    print(*result[i])
