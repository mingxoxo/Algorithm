# 선수과목
# 23.01.21
# 위상정렬(Topology Sort)
# https://www.acmicpc.net/problem/14567

import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def topologySort(graph, N, indegree):
    queue = deque()
    result = [0] * (N + 1)
    for i in range(1, N + 1):
        if indegree[i] == 0:
            result[i] = 1
            queue.append(i)

    while queue:
        sub = queue.popleft()
        for i in graph[sub]:
            indegree[i] -= 1
            if indegree[i] == 0:
                result[i] = result[sub] + 1
                queue.append(i)

    return result[1:]



N, M = map(int, input().split())
graph = defaultdict(list)
indegree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

print(*topologySort(graph, N, indegree))

