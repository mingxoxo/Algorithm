# 문제집
# 22.11.25
# 위상정렬(Topology Sort)
# hhttps://www.acmicpc.net/problem/1766

import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline


def topologySort(graph, N, indegree):
    heap = []
    result = []

    # queue 초기화
    for v in range(1, N + 1):
        if indegree[v] == 0:
            heappush(heap, v)

    while heap:
        n = heappop(heap)
        result.append(n)
        for v in graph[n]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(heap, v)

    return result



N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

print(*topologySort(graph, N, indegree))
