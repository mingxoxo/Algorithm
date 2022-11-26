# 게임 개발
# 22.11.26
# 위상정렬(Topology Sort)
# https://www.acmicpc.net/problem/1516


import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline


def topologySort(graph, N, indegree, time):
    heap = []
    result = [0] * (N + 1)

    # queue 초기화
    for v in range(1, N + 1):
        if indegree[v] == 0:
            heappush(heap, (time[v], v))

    while heap:
        t, n = heappop(heap)
        result[n] = t
        for v in graph[n]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(heap, (t + time[v], v))

    return result[1:]




N = int(input())
indegree = [0] * (N + 1)
time = [0] * (N + 1)
graph = defaultdict(list)
for b in range(1, N + 1):
    infos = list(map(int, input().split()))
    time[b] = infos[0]
    for i in range(1, len(infos) - 1):
        graph[infos[i]].append(b)
        indegree[b] += 1

print(*topologySort(graph, N, indegree, time), sep='\n')
