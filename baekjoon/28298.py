# 더 흔한 타일 색칠 문제
# 23.07.04
# 구현, 그리디
# https://www.acmicpc.net/problem/28298

import sys
input = sys.stdin.readline
from collections import Counter

N, M, K = map(int, input().split())
tile_k = [[[] for _ in range(K)] for _ in range(K)]

for i in range(N):
    tile_row = input().rstrip()
    for j in range(M):
        tile_k[i % K][j % K].append(tile_row[j])

total = N * M
same_k = [[0] * K for _ in range(K)]
for i in range(K):
    for j in range(K):
        ch, cnt = Counter(tile_k[i][j]).most_common()[0]
        same_k[i][j] = ch
        total -= cnt

print(total)
for i in range(N):
    print(''.join(same_k[i % K]) * (M // K))
