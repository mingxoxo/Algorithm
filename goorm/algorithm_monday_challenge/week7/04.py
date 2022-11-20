# 문제 4. 이상한 미로 (FAIL 8개)
# 다익스트라
# 다시 풀어보기

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


def Dijkstra(graph, N, A):
	heap = [(0, 1, 0)]
	visited = [0] * (N + 1)
	visited[1] = -1

	while heap:
		w, n, prev = heapq.heappop(heap)
		if n == N:
			continue
		if w < visited[n]:
			continue
		for x, xw in graph[n]:  # sorted(graph[n], key = lambda x: x[1])
			if visited[x] == 0 or w + xw < visited[x]:
				if prev == 0 or prev % A[n - 1] == x % A[n - 1]:
					visited[x] = w + xw
					heapq.heappush(heap, (w + xw, x, n))

	return visited[N] if visited[N] != 0 else -1


N, M = map(int, input().split())
A = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(M):
	u, v, w = map(int, input().split())
	graph[u].append((v, w))
	graph[v].append((u, w))

print(Dijkstra(graph, N, A))