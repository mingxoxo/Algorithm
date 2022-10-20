# 최소 힙
# 22.10.20
# heapq
# https://www.acmicpc.net/problem/1927

import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    i = int(input())
    if i == 0:
        print(heapq.heappop(heap)) if heap else print("0")
    else:
        heapq.heappush(heap, i)
