# 민준이와 마산 그리고 건우
# Dijkstra
# 22.11.22
# https://www.acmicpc.net/problem/18223

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


def Dijkstra(graph, N, ori, dst):
    if ori == dst:
        return 0

    heap = [(0, ori)]
    visited = [-1] * (N + 1)
    visited[ori] = 0

    while heap:
        w, n = heapq.heappop(heap)
        if visited[n] < w:
            continue
        if n == dst:
            continue
        for x, xw in graph[n]:
            if visited[x] == -1 or w + xw < visited[x]:
                visited[x] = w + xw
                heapq.heappush(heap, (w + xw, x))

    return visited[dst] if visited[dst] != -1 else 0


V, E, P = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

shortest_path = Dijkstra(graph, V, 1, V)
geonwoo_path = Dijkstra(graph, V, 1, P) + Dijkstra(graph, V, P, V)

print("SAVE HIM") if geonwoo_path <= shortest_path else print("GOOD BYE")
