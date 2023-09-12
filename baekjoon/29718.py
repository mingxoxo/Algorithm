# 줄줄이 박수
# 슬라이딩 윈도우
# 23.09.12
# https://www.acmicpc.net/problem/29718

import sys
input=sys.stdin.readline

N, M = map(int, input().split())
clap = []
for _ in range(N):
    clap.append(list(map(int, input().split())))
A = int(input())
column_sum = [sum(column) for column in zip(*clap)]
result = total_sum = sum(column_sum[:A])

for i in range(A, M):
    total_sum += column_sum[i]
    total_sum -= column_sum[i - A]
    result = max(result, total_sum)

print(result)
