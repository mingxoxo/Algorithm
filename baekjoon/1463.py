# 1로 만들기
# DP
# 22.07.25
# https://www.acmicpc.net/problem/1463
# N <= 1000000

import sys

input = sys.stdin.readline

N = int(input())
arr = [0] * (N + 1)

for idx in range(1, N):
    for next_idx in [idx * 3, idx * 2, idx + 1]:
        if next_idx <= N:
            arr[next_idx] = arr[idx] + 1 if arr[next_idx] == 0 else min(arr[next_idx], arr[idx] + 1)

print(arr[N])