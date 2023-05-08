# 합 구하기
# 23.05.08
# https://www.acmicpc.net/problem/11441

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

prefix_sum = [0]
for i in range(N):
    prefix_sum.append(prefix_sum[-1] + A[i])


M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
