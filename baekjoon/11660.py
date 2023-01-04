# 구간 합 구하기 5
# 23.01.05
# 누적합
# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline


def prefix_sum(arr, N):
    psum = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            psum[i][j] = psum[i][j - 1] + psum[i - 1][j] + arr[i - 1][j - 1] - psum[i - 1][j - 1]

    return psum


N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
psum = prefix_sum(arr, N)

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(psum[x2][y2] - psum[x1 - 1][y2] - psum[x2][y1 - 1] + psum[x1 - 1][y1 - 1])
