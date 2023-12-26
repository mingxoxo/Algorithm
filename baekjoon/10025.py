# 게으른 백곰
# 투 포인터
# 23.12.26
# https://www.acmicpc.net/problem/10025

import sys
input=sys.stdin.readline

N, K = map(int, input().split())
buckets = []

for _ in range(N):
    g, x = map(int, input().split())
    buckets.append((x, g))
buckets.sort(key= lambda x: x[0])

start, end = 0, 0
ice_sum = 0
result = 0

while start <= end and end < N:
    if K * 2 < buckets[end][0] - buckets[start][0]:
        ice_sum -= buckets[start][1]
        start += 1
    else:
        ice_sum += buckets[end][1]
        result = max(result, ice_sum)
        end += 1

print(result)
