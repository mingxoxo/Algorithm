# N번째 큰 수
# 우선순위 큐
# 24.09.21
# https://www.acmicpc.net/problem/2075


import heapq

min_heap = []
N = int(input())
for _ in range(N):
    for i in list(map(int, input().split())):
        heapq.heappush(min_heap, i)
        if len(min_heap) > N:
            heapq.heappop(min_heap)


print(min_heap[0])
