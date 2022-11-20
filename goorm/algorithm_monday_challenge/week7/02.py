# 문제 2. 퍼져나가는 소문
# 그래프 탐색
# 컴포넌트 - 무방향 그래프에서 두 정점 u, v 사이에 path가 존재한다면 두 정점은 같은 컴포넌트

import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def BFS(graph):
    queue = deque([1])
    visited = [False] * (N + 1)
    visited[1] = True
    cnt = 1

    while queue:
        n = queue.popleft()
        for x in graph[n]:
            if visited[x] == False:
                visited[x] = True
                cnt += 1
                queue.append(x)

    print(cnt)


N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

BFS(graph)
