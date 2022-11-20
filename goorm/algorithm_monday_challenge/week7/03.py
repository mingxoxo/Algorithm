# 문제 3. 구름이의 여행 2
# BFS / 그래프 이론

import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def BFS(graph, K):
	queue = deque([K])
	visited = [0] * (N + 1)

	while queue:
		n = queue.popleft()
		for x in graph[n]:
			if x == K:
				return visited[n] + 1
			if visited[x] == 0:
				visited[x] = visited[n] + 1
				queue.append(x)

	return -1


N, M, K = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)

print(BFS(graph, K))