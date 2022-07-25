# 계단 오르기
# DP
# 22.07.26
# https://www.acmicpc.net/problem/2579

import sys

input = sys.stdin.readline

N = int(input())
score = [0] + [int(input()) for _ in range(N)]
arr = [{1:0, 2:0} for _ in range(N + 1)]
arr[0] = {0:0}

for i in range(N):
    for cnt, sum in arr[i].items():
        if cnt < 2 and i + 1 <= N:
            arr[i + 1][cnt + 1] = max(arr[i + 1][cnt + 1], sum + score[i + 1])
        if i + 2 <= N:
            arr[i + 2][1] = max(arr[i + 2][1], sum + score[i + 2])

print(max(arr[N][1], arr[N][2]))