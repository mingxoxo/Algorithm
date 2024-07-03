# x
# 24.07.03
# 우선순위 큐
# https://www.acmicpc.net/problem/14235

import sys
import heapq
input=sys.stdin.readline


n = int(input())
pq = []

for _ in range(n):
    base, *value = map(int, input().split())
    if base == 0:
        print(-1 * heapq.heappop(pq)) if pq else print(-1)
        continue
    
    for v in value:
        heapq.heappush(pq, -1 * v)
