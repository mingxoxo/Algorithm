# 음악프로그램
# 22.11.27
# 위상정렬(Topology Sort)
# https://www.acmicpc.net/problem/2623


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
    infos = list(map(int, input().split()))
    for i in range(2, len(infos)):
        graph[infos[i - 1]].append(infos[i])
        indegree[infos[i]] += 1

result = topologySort(graph, N, indegree)
print(*result, sep='\n') if len(result) == N else print(0)
