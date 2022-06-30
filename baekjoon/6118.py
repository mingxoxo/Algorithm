# 숨바꼭질
# 22.06.30
# BFS
# https://www.acmicpc.net/problem/6118

import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph, N):
    visited = [-1] * (N + 1)
    visited[1] = 0
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == -1:
                visited[i] = visited[node] + 1
                queue.append(i)

    distance = max(visited)
    return [visited.index(distance), distance, visited.count(distance)]


N, M = map(int, input().split())
graph = {i : [] for i in range(1, N + 1)}
for _ in range(M):
    ai, bi = map(int, input().split())
    graph[ai].append(bi)
    graph[bi].append(ai)

print(*BFS(graph, N))
