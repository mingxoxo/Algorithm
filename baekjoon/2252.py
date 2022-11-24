# 줄 세우기
# 22.11.24
# 위상정렬(Topology Sort)
# hhttps://www.acmicpc.net/problem/2252


import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def topologySort(graph, N, indegree):
    queue = deque()
    result = []

    # queue 초기화
    for v in range(1, N + 1):
        if indegree[v] == 0:
            queue.append(v)

    while queue:
        n = queue.popleft()
        result.append(n)
        for v in graph[n]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return result


N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

print(*topologySort(graph, N, indegree))
