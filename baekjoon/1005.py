# ACM Craft
# 22.11.23
# 위상정렬(Topology Sort)- heapq ver
# https://www.acmicpc.net/problem/1005


import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline


def topologySort(graph, N, indegree, time, W):
    heap = []

    # queue 초기화
    for v in range(1, N + 1):
        if indegree[v] == 0:
            heappush(heap, (time[v], v))

    while heap:
        t, n = heappop(heap)
        if n == W:
            return t
        for v in graph[n]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(heap, (t + time[v], v))

    return -1


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    indegree = [0] * (N + 1)
    graph = defaultdict(list)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1
    W = int(input())
    print(topologySort(graph, N, indegree, time, W))
