# ACM Craft
# 22.11.23
# 위상정렬(Topology Sort)
# https://www.acmicpc.net/problem/1005


import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline


def topologySort(graph, N, indegree, time, W):
    total_time = [0] * (N + 1)
    queue = deque()

    # queue 초기화
    for v in range(1, N + 1):
        if indegree[v] == 0:
            queue.append(v)
            total_time[v] = time[v]

    while queue:
        n = queue.popleft()
        if n == W:
            return total_time[n]
        for v in graph["out"][n]:
            indegree[v] -= 1
            total_time[v] = max(total_time[v], total_time[n] + time[v])
            if indegree[v] == 0:
                queue.append(v)

    return total_time[n]




T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    indegree = [0] * (N + 1)
    graph = { key: [[] for j in range(N + 1)] for key in ["in", "out"]}
    for _ in range(K):
        X, Y = map(int, input().split())
        graph["out"][X].append(Y)
        graph["in"][Y].append(X)
        indegree[Y] += 1
    W = int(input())
    print(topologySort(graph, N, indegree, time, W))
