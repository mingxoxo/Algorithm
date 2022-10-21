# 최대 힙
# heapq
# 22.10.21
# https://www.acmicpc.net/problem/11279

import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    i = int(input())
    if i == 0:
        print(heapq.heappop(heap)[1]) if heap else print("0")
    else:
        heapq.heappush(heap, (-i, i))
