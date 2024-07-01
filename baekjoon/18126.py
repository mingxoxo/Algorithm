# 너구리 구구
# 24.07.01
# 트리 탐색
# https://www.acmicpc.net/problem/18126
# 입구과 모든 방들은 총 N-1개의 길로 서로 오고 갈 수 있다. -> 트리라는 이야기!

import sys
input=sys.stdin.readline

from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]

dist = [-1 for _ in range(N + 1)]
dist[1] = 0

for _ in range(N - 1):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

queue = deque([1])
while queue:
    from_node = queue.popleft()
    for to_node, d in graph[from_node]:
        if dist[to_node] == -1:
            dist[to_node] = dist[from_node] + d
            queue.append(to_node)

print(max(dist))
