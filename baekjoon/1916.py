# 최소비용 구하기
# Dijkstra
# 22.11.18
# https://www.acmicpc.net/problem/1916
# 다시 풀 필요가 있음

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


def Dijkstra(graph, ori, dst, N):
    heap = [(0, ori)]
    visited = [-1] * (N + 1)
    visited[ori] = 0

    while heap:
        w, n = heapq.heappop(heap)
        if n == dst:
            break
        for x, xw in graph[n]:
            if visited[x] == -1 or w + xw < visited[x]:
                visited[x] = w + xw
                heapq.heappush(heap, (w + xw, x))

    return visited[dst]


N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    ori, dst, w = map(int, input().split())
    graph[ori].append((dst, w))

# (1, 2, 2), (1, 2, 5), (1, 2, 3), (1, 2, 2)
for i in range(M):
    graph[i].sort(key=lambda x: x[1])

ori, dst = map(int, input().split())
print(Dijkstra(graph, ori, dst, N))
