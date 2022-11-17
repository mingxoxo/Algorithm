# 최단경로
# Dijkstra
# 22.11.17
# https://www.acmicpc.net/problem/1753

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


def Dijkstra(graph, V, K):
    heap = [(0, K)]
    visited = [-1] * (V + 1)
    visited[K] = 0

    while heap:
        w, n = heapq.heappop(heap)
        for x, xw in graph[n]:
            if visited[x] == -1 or w + xw < visited[x]:
                visited[x] = w + xw
                heapq.heappush(heap, (w + xw, x))

    return [visited[i] if visited[i] != -1 else "INF" for i in range(1, V + 1)]


V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

print(*Dijkstra(graph, V, K), sep='\n')
