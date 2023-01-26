# 바닥 장식
# 23.01.26
# 그래프 탐색
# https://www.acmicpc.net/problem/1388

import sys
from collections import deque, defaultdict
input = sys.stdin.readline


N, M = map(int, input().split())
shape = []
for _ in range(N):
    shape.append(input().rstrip())

cnt = 0

for i in range(N):
    for j in range(M):
        if shape[i][j] == '-':
            if j + 1 < M and shape[i][j + 1] == '-':
                continue
            cnt += 1
        elif shape[i][j] == '|':
            if i + 1 < N and shape[i + 1][j] == '|':
                continue
            cnt += 1

print(cnt)
