#24444
#알고리즘 수업 - 너비 우선 탐색 1
#https://www.acmicpc.net/problem/24444

import sys
from collections import deque

def BFS(graph, R, N):
    visited = [0] * (N + 1)
    visited[R] = 1
    queue = deque([R])
    cnt = 2
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = cnt
                cnt += 1
                queue.append(i)
    return visited[1:]


input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

graph = [sorted(i) for i in graph]
result = BFS(graph, R, N)
for i in result:
    print(i)
