# 수 고르기
# 22.08.04
# 투포인터
# https://www.acmicpc.net/problem/2230

import sys
input = sys.stdin.readline


def two_pointer(N, M, arr):
    start, end = 0, 0
    result = arr[-1] - arr[0]
    while start <= end and end < N:
        if arr[end] - arr[start] < M:
            end += 1
        else:
            result = min(result, arr[end] - arr[start])
            start += 1
    return result

N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
print(two_pointer(N, M, arr))
