# 알고리즘 수업 - 깊이 우선 탐색 2
# 그래프 / DFS / 정렬
# 22.11.11
# https://www.acmicpc.net/problem/24480

import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(graph, R, visited, cnt):
    visited[R] = cnt
    for x in graph[R]:
        if visited[x] == 0:
            cnt = DFS(graph, x, visited, cnt + 1)

    return cnt


N, M, R = map(int, input().split())
graph = defaultdict(list)
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

DFS(graph, R, visited, 1)
print(*visited[1:], sep='\n')
